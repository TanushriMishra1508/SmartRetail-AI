import pandas as pd


def clean_data(df):
    """
    Clean the retail dataset.
    """

    print("\nStarting Data Cleaning...\n")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicates}")

    df = df.drop_duplicates()

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    print("\nData Types:\n")
    print(df.dtypes)

    return df