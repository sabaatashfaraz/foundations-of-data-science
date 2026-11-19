# Assignment 2 — Data Extraction and Statistical Hypothesis Testing

This assignment explores a data-collection-to-analysis workflow using restaurant information from six New York City neighborhoods.

## Main workflow

1. Collect restaurant information for the neighborhoods specified in the notebook.
2. Parse and structure the extracted fields.
3. Store the resulting records in a SQLite database.
4. Query the database with SQL.
5. Use Pandas and statistical methods to compare restaurant characteristics across neighborhoods.

## Analysis themes

- Restaurant price-range distributions across neighborhoods.
- Cuisine-type frequency and neighborhood-level comparisons.
- Restaurant ratings and review counts.
- Statistical comparisons, including independent-sample t-tests where specified in the notebook.
- Visualization and interpretation of restaurant-level data.

## Main tools

Python, Selenium, `undetected_chromedriver`, Beautiful Soup, SQLite, Pandas, NumPy, Matplotlib, Seaborn, and SciPy.

## Notebook

`assignment_02_data_extraction_hypothesis_testing.ipynb`

## Data and browser setup

The original notebook creates `restaurants.csv` and `restaurants.db`. These collected data files are not included in this public repository copy.

The browser-automation section requires a compatible Chrome installation and browser-driver dependencies. **Before running it, review the target website's current terms of service, robots/access rules, and applicable law. Do not bypass access controls, CAPTCHAs, or other technical restrictions.** Prefer an approved API or a dataset that is explicitly licensed for reuse.

## Run

From this assignment directory:

```bash
pip install -r ../../requirements/assignment-02.txt
jupyter lab
```

Place any permitted input/export files in the local `data/` directory and update notebook paths as needed.
