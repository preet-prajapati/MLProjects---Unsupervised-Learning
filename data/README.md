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

The project owner has confirmed that this is a randomly generated/synthetic dataset created for
educational analysis. It does not describe real SmartCart customers. The file contains no names, email
addresses, phone numbers, or street addresses.

Keep the repository synthetic: do not replace this file with live customer records without an appropriate
privacy, security, and governance review. The repository's MIT License covers the code and documentation;
dataset reuse terms have not been specified separately by the project owner.
