
import pandas as pd
import numpy as np
import sys

def preprocess_data(input_path, output_path):

    df = pd.read_excel(input_path)
    df.columns = df.columns.str.lower().str.replace('.', '_').str.strip()
    
    required_cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
    
    cols_to_keep = [col for col in required_cols if col in df.columns]
    df = df[cols_to_keep]

    if 'survived' in df.columns:
        df['survived'] = pd.to_numeric(df['survived'], errors='coerce')
    
    numeric_cols = ['pclass', 'age', 'sibsp', 'parch', 'fare']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median())
    
    if 'fare' in df.columns:
        fare_mean = df['fare'].mean()
        df['fare'] = df['fare'].fillna(fare_mean)
    
    if 'embarked' in df.columns:
        embarked_mode = df['embarked'].mode()[0] if not df['embarked'].mode().empty else 'S'
        df['embarked'] = df['embarked'].fillna(embarked_mode)
    
    if 'sex' in df.columns:
        df['sex'] = df['sex'].str.lower().str.strip()
        df['sex'] = df['sex'].map({'male': 1, 'female': 0})
        df['sex'] = pd.to_numeric(df['sex'], errors='coerce')
        df['sex'] = df['sex'].fillna(0).astype(int)
    
    # One-hot encode Embarked
    if 'embarked' in df.columns:
        df['embarked'] = df['embarked'].str.upper().str.strip()
        df = pd.get_dummies(df, columns=['embarked'], drop_first=True, dtype=int)
    
    df = df.dropna()
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df = df.dropna()  
    
    int_cols = ['survived', 'pclass', 'sex', 'sibsp', 'parch'] + [col for col in df.columns if col.startswith('embarked_')]
    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].astype(int)
    
    df.to_csv(output_path, index=False)
    

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "data/raw/titanic.xls"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "data/processed/titanic_processed.csv"
    
    preprocess_data(input_path, output_path)
