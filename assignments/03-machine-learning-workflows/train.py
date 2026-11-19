
import pandas as pd
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import sys

def train_model(input_path, model_path, metrics_path):

    df = pd.read_csv(input_path)
    
    X = df.drop('survived', axis=1)
    y = df['survived']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # logistic regression 
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    
    # predictions
    y_pred = model.predict(X_test)
    
    # metrics
    metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred)),
        'recall': float(recall_score(y_test, y_pred)),
        'f1_score': float(f1_score(y_test, y_pred)),
        'train_size': int(len(X_train)),
        'test_size': int(len(X_test))
    }
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    # metrics as JSON
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    
    for metric, value in metrics.items():
        if isinstance(value, float):
            print(f"{metric}: {value:.4f}")
        else:
            print(f"{metric}: {value}")

if __name__ == "__main__":

    input_path = sys.argv[1] if len(sys.argv) > 1 else "data/processed/titanic_processed.csv"
    model_path = sys.argv[2] if len(sys.argv) > 2 else "models/model.pkl"
    metrics_path = sys.argv[3] if len(sys.argv) > 3 else "metrics.json"
    
    train_model(input_path, model_path, metrics_path)
