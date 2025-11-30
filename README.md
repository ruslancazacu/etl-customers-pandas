# Data Pipeline — Customers (Pandas)

Mini-pipeline pentru curățare clienți (email, duplicate, date) și încărcare în SQLite.

## Run
```bash
python -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt
python src/pipeline.py
