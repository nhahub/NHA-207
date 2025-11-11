import pandas as pd
# clean column name
def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "").str.lower()
    return df


# Remove extra spaces and standardize capitalization in categorical columns
def clean_categorical(df: pd.DataFrame, cat_cols: list[str]) -> pd.DataFrame:
    for cat in cat_cols:
         df[cat] = df[cat].astype(str).str.strip().str.title()
    return df
