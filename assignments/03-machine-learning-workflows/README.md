# Assignment 3 — Machine Learning and Data Science Workflows

This assignment combines foundational machine-learning algorithms with model evaluation, time-series modeling, graph methods, and a reproducible data pipeline.

## Sections represented in the notebook

1. **Multiclass Support Vector Machine:** vectorized SVM loss and gradient, numerical gradient checking, SGD training, and visualization of learned weights.
2. **k-Nearest Neighbors:** classifier implementation, distance-matrix computation, vectorization, and runtime comparison.
3. **Customer segmentation:** feature scaling and K-Means clustering.
4. **Dimensionality reduction:** PCA and t-SNE, including visualization and interpretation of lower-dimensional representations.
5. **Model selection:** Decision Tree classification and hyperparameter tuning with `GridSearchCV`.
6. **Multivariate time-series AutoML:** lag-feature construction and H2O AutoML forecasting.
7. **Multilayer Perceptron:** supervised neural-network modeling and evaluation.
8. **LSTM:** sequence preparation and recurrent time-series modeling.
9. **DVC pipeline:** a two-stage workflow for preprocessing Titanic data and training/evaluating a Logistic Regression model.
10. **Personalized PageRank:** sparse-matrix operations and personalized ranking.

## Main tools

Python, NumPy, Pandas, Matplotlib, Seaborn, SciPy, scikit-learn, TensorFlow/Keras, H2O AutoML, and DVC.

## Files

- `assignment_03_machine_learning_workflows.ipynb` — main coursework notebook.
- `preprocess.py` — Titanic data-cleaning stage for the DVC example.
- `train.py` — Logistic Regression training and metric-generation stage.
- `dvc.yaml` and `dvc.lock` — recorded DVC pipeline definition and lock state.
- `metrics.json` — metrics file from the supplied assignment bundle.

## Expected input data

The notebook expects some local files that are not bundled in this public portfolio copy:

- `data.csv` — point dataset used in the Decision Tree/Grid Search section.
- `Movies_input.xlsx` — input for the PCA/t-SNE section.
- `pollution.csv` — air-pollution time-series input used by the H2O AutoML section.
- `airline-passengers.csv` — univariate time-series input used by the LSTM section.
- `data/raw/titanic.xls` — input for the DVC preprocessing/training pipeline.

The customer-segmentation section downloads its dataset from the IBM-hosted URL already present in the notebook. Place the other permitted files in the paths expected by the notebook, or update the paths to match your local organization.

## Run the DVC pipeline

From this assignment directory, place an authorized `titanic.xls` file at `data/raw/titanic.xls`, then install the dependencies and run:

```bash
pip install -r ../../requirements/assignment-03.txt
dvc repro
```

A compatible Java runtime is required for the H2O AutoML section. The DVC cache, input datasets, and generated model binary are not included. If you want to share DVC-managed data, configure a DVC remote and use `dvc push`/`dvc pull` rather than committing cache directories.

## Run the notebook

```bash
jupyter lab
```

Run cells in order and check that each required dataset is available before executing the corresponding section.
