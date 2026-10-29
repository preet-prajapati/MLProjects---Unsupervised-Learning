from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "smartcart_customers.csv"

REQUIRED_COLUMNS = {
    "ID",
    "Year_Birth",
    "Education",
    "Marital_Status",
    "Income",
    "Kidhome",
    "Teenhome",
    "Dt_Customer",
    "Recency",
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds",
    "NumDealsPurchases",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",
    "NumWebVisitsMonth",
    "Complain",
    "Response",
}

SPEND_COLUMNS = {
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds",
}


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def test_required_schema_and_unique_ids():
    data = load_data()
    assert REQUIRED_COLUMNS.issubset(data.columns)
    assert data["ID"].notna().all()
    assert data["ID"].is_unique
    assert not data.duplicated().any()


def test_dates_are_parseable():
    data = load_data()
    parsed_dates = pd.to_datetime(data["Dt_Customer"], dayfirst=True, errors="raise")
    assert parsed_dates.notna().all()


def test_spending_values_are_nonnegative():
    data = load_data()
    assert data[list(SPEND_COLUMNS)].ge(0).all().all()


def test_income_can_be_median_imputed():
    data = load_data()
    imputed_income = data["Income"].fillna(data["Income"].median())
    assert imputed_income.notna().all()
    assert imputed_income.gt(0).all()
