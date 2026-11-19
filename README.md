# Foundations of Data Science — Coursework Portfolio

A curated collection of programming assignments completed for **Foundations of Data Science** at **Sharif University of Technology**.

**Author:** Saba Atashfaraz  
**Program:** B.Sc. Electrical Engineering — Communications Systems  
**Course:** Foundations of Data Science  
**Institution:** Sharif University of Technology  
**Term:** Fall 2025  
**Instructor:** Dr. Khalaj  
**Course grade:** 20/20

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

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/foundations-of-data-science.git
cd foundations-of-data-science
```

Replace `<YOUR_GITHUB_USERNAME>` with your GitHub username.

### 2. Create an environment

Python **3.10 or 3.11** is a practical starting point. The assignments use different ML frameworks, so separate environments are recommended rather than installing every dependency at once.

**Windows**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies for the assignment you want to run

For example, Assignment 1:

```bash
python -m pip install --upgrade pip
pip install -r requirements/assignment-01.txt
jupyter lab
```

Use the corresponding requirements file for Assignments 2, 3, or 4. The top-level `requirements.txt` installs the combined dependency set and may be substantially larger.

### 4. Open a notebook

Launch JupyterLab and open the relevant `.ipynb` file. Read the assignment-specific README and data notes first; some original course datasets are not included in this public portfolio copy.

## Data, execution, and reproducibility

To keep the repository focused and avoid redistributing third-party or course-provided data without confirmed permission, the original input datasets are **not bundled**. Each assignment's `data/README.md` describes the expected files and paths.

- **Assignment 1:** expects several course datasets under `data/Q1` through `data/Q6`. The Books to Scrape exercise retrieves data from the practice website and creates `books_scraped.csv`.
- **Assignment 2:** the notebook creates and queries a restaurant dataset and SQLite database. The collected `restaurants.csv` and `restaurants.db` are not included. The notebook's saved outputs have been cleared to avoid publishing collected third-party restaurant records.
- **Assignment 3:** several sections expect local CSV/Excel inputs. The customer-segmentation section downloads its dataset from the URL in the notebook. The DVC example expects a Titanic Excel file at `data/raw/titanic.xls`; see the assignment README before running the pipeline.
- **Assignment 4:** the notebooks use `torchvision.datasets.MNIST` with `download=True`, so MNIST is downloaded automatically when the relevant cells are executed. Generated image archives and downloaded datasets are not included.

Notebook outputs are retained where useful, except for Assignment 2. Personal student identifiers and machine-specific file paths have been removed from the public-facing notebook copies. The code has not been re-executed as part of packaging, so dependencies, data paths, and external services may need adjustment in a fresh environment.

### DVC workflow in Assignment 3

After placing an authorized copy of `titanic.xls` at `assignments/03-machine-learning-workflows/data/raw/titanic.xls`, install the Assignment 3 requirements and run the pipeline from that assignment directory:

```bash
cd assignments/03-machine-learning-workflows
dvc repro
```

The pipeline is defined in `dvc.yaml` and uses `preprocess.py` followed by `train.py`. The input dataset and DVC cache are not included. To share DVC-managed data with collaborators, configure a DVC remote and follow the DVC data-versioning workflow.

## Environment notes

- Assignment 2 requires a compatible Chrome installation for its browser-automation exercise. Check the website's current terms and access rules before running any scraper.
- Assignment 3's H2O AutoML section requires a compatible Java runtime.
- GPU acceleration is optional for the deep-learning notebooks, but training time may be longer on CPU.
- Some notebook cells use relative paths or course-specific files; run them from the relevant assignment directory and update paths if necessary.

## Academic and sharing note

This repository is a personal record of coursework. Course prompts, datasets, and third-party materials may be subject to their original licenses and course policies. See [SHARING_AND_ACADEMIC_INTEGRITY.md](SHARING_AND_ACADEMIC_INTEGRITY.md) before making the repository public or reusing any material.

---

**Topics represented:** Data Science · Statistical Analysis · Machine Learning · Deep Learning · Generative Models · Neural Architecture Search · Reproducible ML
