# Assignment 1 — Data Manipulation and Visualization

This assignment focuses on the practical Python tools used in data science, with an emphasis on loading, cleaning, transforming, querying, and visualizing real-world datasets.

## Topics and exercises

1. **Business transactions:** loading multi-sheet Excel data, cleaning transaction records, and answering questions about transaction dates and branch activity.
2. **Canadian Cheese Directory:** data wrangling, categorical-variable handling, querying, and interpretation.
3. **Business analyst job listings:** cleaning job-posting fields, parsing salary and company information, handling inconsistent ratings and company sizes, and visualizing patterns.
4. **COVID-19 polling:** reproducing and interpreting time-series visualizations from polling data.
5. **Bookstore web scraping:** extracting book titles, prices, ratings, and categories from [Books to Scrape](https://books.toscrape.com/) using Requests and Beautiful Soup.
6. **Titanic exploratory analysis (bonus):** examining passenger attributes, categorical variables, distributions, and survival-related patterns.

## Main tools

Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Requests, Beautiful Soup, scikit-learn preprocessing utilities, and WordCloud.

## Notebook

`assignment_01_data_manipulation_visualization.ipynb`

## Expected input data

The original notebook uses relative paths for course datasets. Place authorized copies in the following structure:

```text
data/
├── Q1/
│   └── E-commerce_data.xlsx
├── Q2/
│   └── cheese_data.csv
├── Q3/
│   ├── BusinessAnalyst.csv
│   └── adjectives.txt
├── Q4/
│   └── covid/
│       └── covid-19-polls-master/
│           ├── covid_approval_polls.csv
│           ├── covid_approval_toplines.csv
│           └── covid_concern_polls.csv
└── Q6/
    ├── titanic.xls
    └── titanic.html
```

The transaction workbook and other course datasets are not included in this repository. The bookstore exercise accesses the practice website and writes `books_scraped.csv` when run.

## Run

From this assignment directory:

```bash
pip install -r ../../requirements/assignment-01.txt
jupyter lab
```

**Portability note:** some original path strings use Windows-style backslashes. On macOS or Linux, convert those paths to `pathlib.Path` or use forward slashes.
