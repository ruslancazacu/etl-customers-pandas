import pandas as pd
from src.transform import clean_emails, drop_duplicates, standardize_dates, transform

def sample_df():
    return pd.DataFrame([
        {"name":"Ana","email":" Ana@ExAMPLE.COM ","phone":"111","signup_date":"2025-01-01","country":"CH"},
        {"name":"Ana","email":"ana@example.com","phone":"111","signup_date":"2025-01-01","country":"CH"},
        {"name":"Bob","email":"bob@example.com","phone":"222","signup_date":"not_a_date","country":None},
    ])

def test_clean_emails():
    out = clean_emails(sample_df())
    assert out.loc[0,"email"] == "ana@example.com"

def test_drop_duplicates():
    out = drop_duplicates(sample_df())
    assert len(out) == 2

def test_standardize_dates():
    out = standardize_dates(sample_df())
    assert str(out.loc[0,"signup_date"]).startswith("2025-01-01")
    assert pd.isna(out.loc[2,"signup_date"])

def test_transform_full():
    out = transform(sample_df())
    assert out["country"].iloc[-1] == "Unknown"
