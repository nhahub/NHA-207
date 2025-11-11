import pandas as pd
# clean column name
def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "").str.lower()
    return df


# Checking for null values in each column and duplicate rows check unique values in the id column
def check_nulls_duplicates(df: pd.DataFrame, id_col: str) -> None:
    nulls = df.isnull().sum()
    duplicates = df.duplicated().sum()
    unique_ids = df[id_col].nunique()
    
    duplicate_id_count = df.shape[0] - unique_ids
    
    if duplicate_id_count > 0:
        print(f"Warning: There are {duplicate_id_count} duplicate values in the '{id_col}' column.")
    
    print("Null values in each column:")
    print(nulls)
    
    print(f"\nDuplicate rows: {duplicates}")
    print(f'Unique IDs of the Total cells {df.shape[0]} is: {unique_ids}')



# Remove extra spaces and standardize capitalization in categorical columns
def clean_categorical(df: pd.DataFrame, cat_cols: list[str]) -> pd.DataFrame:
    for cat in cat_cols:
         df[cat] = df[cat].astype(str).str.strip().str.title()
    return df
