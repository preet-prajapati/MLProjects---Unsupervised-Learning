# Contributing

Small, focused improvements are welcome. Before opening a pull request:

1. Create a branch from `main`.
2. Keep the notebook reproducible from a clean environment.
3. Do not commit notebook checkpoints, local environments, credentials, or private customer data.
4. Run `pytest -q tests`.
5. Run `pytest --nbmake --nbmake-timeout=300 notebooks/smartcart_customer_segmentation.ipynb`.
6. Explain any changes to features, outlier rules, cluster count, or evaluation metrics in the pull
   request description.

If the dataset changes, update `data/README.md` with a verified source citation, applicable license,
and any material schema or privacy changes.
