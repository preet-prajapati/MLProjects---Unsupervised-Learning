# Dataset notes

`raw/smartcart_customers.csv` is the de-identified customer dataset supplied with the original
SmartCart project. It contains 2,240 rows and 22 fields covering demographics, household structure,
purchase behavior, and campaign outcomes.

## Data quality

- Customer IDs are unique, and there are no duplicate rows.
- `Income` contains 24 missing values; the notebook uses median imputation.
- Three birth years are implausible and one income value is extreme; the notebook documents and removes
  those four observations before clustering.
- The latest customer-enrollment date is 2014-06-29, which is used as the reference date for age.

## Privacy and provenance

The file has no names, email addresses, phone numbers, or street addresses, but it still contains a
pseudonymous customer identifier plus income, household, and purchase information. Handle it as
sensitive analytical data and do not attempt to re-identify individuals.

The original project did not record the dataset's source URL or redistribution terms. The repository's
MIT License covers the code and documentation; it does **not** establish rights to reuse this dataset.
Before redistributing or using the data outside this project, add a verified source citation and confirm
the applicable data license.
