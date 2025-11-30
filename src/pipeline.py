import pandas as pd
import sqlite3
from pathlib import Path
from transform import transform

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "customers.csv"
OUT = ROOT / "data" / "processed" / "customers_clean.csv"
DB  = ROOT / "data" / "processed" / "warehouse.sqlite"

def main():
    df = pd.read_csv(RAW)
    clean = transform(df)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(OUT, index=False)

    conn = sqlite3.connect(DB)
    clean.to_sql("customers", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Saved: {OUT}")
    print(f"SQLite: {DB} (table customers)")

if __name__ == "__main__":
    main()
