# Dataset inventory and redistribution notes

The repository intentionally excludes input datasets and generated binary artifacts where their provenance or redistribution permission was not established.

| Assignment | Expected data / artifacts | Included? |
|---|---|---|
| 01 | E-commerce workbook, Canadian cheese CSV, Business Analyst CSV, adjective list, COVID polling files, Titanic files | No |
| 01 | `books_scraped.csv` generated from Books to Scrape | No |
| 02 | `restaurants.csv` and `restaurants.db` generated from restaurant collection | No |
| 03 | `data.csv`, `Movies_input.xlsx`, `pollution.csv`, `airline-passengers.csv`, Titanic source workbook | No |
| 03 | `dvc.yaml`, `dvc.lock`, preprocessing/training scripts, metrics JSON | Yes |
| 04 | MNIST raw files | No; downloaded by torchvision |
| 04 | generated image archive | No |

Consult the README inside each assignment folder for expected relative paths and setup notes. Obtain datasets from their original course or public source, verify terms, and only then add them to a public repository.
