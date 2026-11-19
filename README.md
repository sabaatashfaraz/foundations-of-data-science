# Foundations of Data Science — Coursework Portfolio

A curated collection of programming assignments completed for **Foundations of Data Science** at **Sharif University of Technology**.

**Author:** Saba Atashfaraz  
**Program:** B.Sc. Electrical Engineering — Communications Systems  
**Course:** Foundations of Data Science  
**Institution:** Sharif University of Technology  
**Term:** Fall 2025  
**Instructor:** Dr. Khalaj  

This repository documents a progression from practical data acquisition and exploratory analysis to statistical inference, classical machine learning, deep learning, generative modeling, neural architecture search, and reproducible ML workflows.

The notebooks are presented as a coursework portfolio. They are not intended to be a production-ready software package or an official distribution of course materials.

---

## Assignment overview

| Assignment | Focus | Main techniques |
|---|---|---|
| [01 — Data Manipulation & Visualization](assignments/01-data-manipulation-visualization/) | Data wrangling, cleaning, exploration, visualization, and web scraping | Python, Pandas, NumPy, Matplotlib, Seaborn, Beautiful Soup, descriptive statistics |
| [02 — Data Extraction & Hypothesis Testing](assignments/02-data-extraction-hypothesis-testing/) | Collecting restaurant data, structuring it in a relational database, and analyzing differences across neighborhoods | Selenium, Beautiful Soup, SQLite, SQL, Pandas, SciPy, statistical hypothesis testing |
| [03 — Machine Learning Workflows](assignments/03-machine-learning-workflows/) | Classical ML, dimensionality reduction, time-series modeling, AutoML, graph ranking, and reproducible pipelines | SVM, kNN, K-Means, PCA, t-SNE, GridSearchCV, H2O AutoML, MLP, LSTM, DVC, Personalized PageRank |
| [04 — Generative Models & Neural Architecture Search](assignments/04-generative-models-and-nas/) | Probabilistic generative models, adversarial learning, and automated neural-network design | VAE, β-VAE, CVAE, DCGAN, WGAN, WGAN-GP, CGAN, FID/IS, spectral normalization, AdaIN, random/evolutionary search, DARTS |

## What this portfolio demonstrates

- **Data handling:** loading, cleaning, transforming, querying, and validating structured datasets.
- **Exploratory data analysis:** summarizing distributions, examining relationships, and communicating findings through visualizations.
- **Statistical reasoning:** formulating comparisons and applying statistical tests to real-world data.
- **Machine learning:** implementing and evaluating classification, clustering, dimensionality-reduction, and model-selection methods.
- **Deep learning:** working with multilayer perceptrons, recurrent models, convolutional networks, and generative architectures.
- **Research-oriented experimentation:** comparing methods, interpreting model behavior, and exploring trade-offs between predictive performance and computational cost.
- **Reproducibility:** structuring preprocessing and training stages with DVC.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── requirements/
│   ├── assignment-01.txt
│   ├── assignment-02.txt
│   ├── assignment-03.txt
│   └── assignment-04.txt
├── .gitignore
├── SHARING_AND_ACADEMIC_INTEGRITY.md
└── assignments/
    ├── 01-data-manipulation-visualization/
    │   ├── README.md
    │   ├── assignment_01_data_manipulation_visualization.ipynb
    │   └── data/README.md
    ├── 02-data-extraction-hypothesis-testing/
    │   ├── README.md
    │   ├── assignment_02_data_extraction_hypothesis_testing.ipynb
    │   └── data/README.md
    ├── 03-machine-learning-workflows/
    │   ├── README.md
    │   ├── assignment_03_machine_learning_workflows.ipynb
    │   ├── dvc.yaml
    │   ├── dvc.lock
    │   ├── preprocess.py
    │   ├── train.py
    │   ├── metrics.json
    │   └── data/
    │       └── README.md
    └── 04-generative-models-and-nas/
        ├── README.md
        ├── 01_variational_autoencoders.ipynb
        ├── 02_generative_adversarial_networks.ipynb
        └── 03_neural_architecture_search.ipynb
```
