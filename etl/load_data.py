import pandas as pd
from clean_data import clean_data


def load_dataset(file_path):
    """
    Load the retail sales dataset.
    """

    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")

        print("✅ Dataset Loaded Successfully!\n")
        print(df.head())

        # Clean the data
        df = clean_data(df)

        return df

    except FileNotFoundError:
        print("❌ File not found!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    dataset_path = "data/raw/Sample - Superstore.csv"
    load_dataset(dataset_path)