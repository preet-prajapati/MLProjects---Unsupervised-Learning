# MLProjects — Unsupervised Learning

[![Validate SmartCart project](https://github.com/preet-prajapati/MLProjects---Unsupervised-Learning/actions/workflows/notebook-ci.yml/badge.svg)](https://github.com/preet-prajapati/MLProjects---Unsupervised-Learning/actions/workflows/notebook-ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end, reproducible customer-segmentation project using SmartCart marketing data. The analysis
prepares customer and purchase features, selects a cluster count, compares K-Means with agglomerative
clustering, and turns the selected solution into interpretable customer profiles.

## Project highlights

- Validates a 2,240-row dataset and documents its missing values and outlier rules.
- Engineers age, tenure, total spending, household size, education, and living-status features.
- Keeps campaign `Response` and `Complain` outcomes out of model fitting to avoid circular profiles.
- Fits clusters on all 15 standardized model features; PCA is used only for visualization.
- Uses both elbow and silhouette diagnostics and compares two algorithms with three validation metrics.
- Includes data-contract tests and a GitHub Actions workflow that executes the notebook on every push.

## Results

The elbow method selects **four clusters**. K-Means is retained because it performs better than the
agglomerative candidate on all three reported internal diagnostics for this feature set.

| Model | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ |
|---|---:|---:|---:|
| **K-Means** | **0.183** | **1.722** | **404.859** |
| Agglomerative | 0.169 | 1.917 | 347.973 |

The three-component PCA view retains **51.68%** of standardized variance. Because it is incomplete, it
is intentionally not used for fitting the clusters.

### Exploratory segment profiles

| Cluster | Descriptive profile | Customers | Share | Avg. income | Avg. spending | Response rate |
|---:|---|---:|---:|---:|---:|---:|
| 0 | Younger, moderate-spend households | 214 | 9.6% | 35,426 | 245 | 6.1% |
| 1 | Budget-conscious family households | 660 | 29.5% | 38,077 | 195 | 9.2% |
| 2 | High-value, high-engagement customers | 787 | 35.2% | 73,211 | 1,277 | 23.0% |
| 3 | Established mid-income family households | 575 | 25.7% | 44,935 | 294 | 13.7% |

These names are analyst-friendly summaries, not fixed customer identities. Cluster numbers and profiles
can change when the data, features, scaling, or random seed change.

## Repository structure

```text
.
├── .github/workflows/notebook-ci.yml
├── data/
│   ├── README.md
│   └── raw/smartcart_customers.csv
├── notebooks/smartcart_customer_segmentation.ipynb
├── tests/test_data_contract.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements-dev.txt
└── requirements.txt
```

## Methodology

1. Validate the required schema, unique customer IDs, and missing-value pattern.
2. Median-impute the 24 missing income values.
3. Calculate age at the dataset's latest enrollment year (2014), customer tenure, total spending, and
   total children.
4. Consolidate education and living-status categories and remove four documented outliers.
5. Hold out campaign response and complaint flags, one-hot encode the remaining categories, and
   standardize all model features.
6. Use PCA for a three-dimensional visualization only.
7. Select `k=4` from the elbow diagnostic, while reporting the silhouette trade-off.
8. Compare K-Means and Ward-linkage agglomerative clustering in the full standardized feature space.
9. Profile the selected clusters in the original business units.

## Run locally

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install dependencies and open the notebook:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab notebooks/smartcart_customer_segmentation.ipynb
```

Run the validation suite:

```bash
pip install -r requirements-dev.txt
pytest -q tests
pytest --nbmake --nbmake-timeout=300 notebooks/smartcart_customer_segmentation.ipynb
```

## Data and responsible use

The dataset is de-identified, but it contains a pseudonymous ID plus income, household, and purchasing
information. Do not attempt to re-identify individuals or use exploratory clusters for high-impact
eligibility decisions.

The original project did not record the dataset source URL or redistribution terms. See
[data/README.md](data/README.md) before reusing or redistributing the data. The observations are also
historical—the latest enrollment date is in 2014—so the profiles must be revalidated on current data
before operational use.

## License

The code and documentation are available under the [MIT License](LICENSE). This license does not
establish reuse rights for the dataset; its original source and terms should be verified separately.

