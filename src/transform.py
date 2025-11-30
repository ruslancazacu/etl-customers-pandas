import pandas as pd

def clean_emails(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["email"] = df["email"].astype(str).str.strip().str.lower()
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=["email"])
    df = df.drop_duplicates(subset=["name","phone"])
    return df

def standardize_dates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_emails(df)
    df = drop_duplicates(df)
    df = standardize_dates(df)
    df["country"] = df["country"].fillna("Unknown")
    return df
