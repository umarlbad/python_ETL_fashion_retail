from utils.extract import scraping_data
from pathlib import Path
from utils.transform import transform_data
from utils.load import load_data, load_to_google_sheets, load_to_postresql

BASE_URL = "https://fashion-studio.dicoding.dev"
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "fashion_products.csv"
CREDENTIALS_FILE = BASE_DIR/"google-sheets-api.json"
SPREADSHEET_ID = "1wOObbEOk2iWoevoGdC5j7zBu_EinKpChHWPpkAMVUyg"
def main():
    try:
        print("=" * 50)
        print("STARTING ETL PIPELINE")
        print("=" * 50)

        # Extract
        print("\n[1/3] Extracting data...")
        raw_df = scraping_data(BASE_URL)
        print(raw_df.shape)
        print(raw_df.head())
        print(f"Extracted {len(raw_df)} rows")

        # Transform
        print("\n[2/3] Transforming data...")
        clean_df = transform_data(raw_df)
        print(f"Cleaned data: {len(clean_df)} rows")
        print(clean_df.isna().sum())
        print(clean_df[clean_df["title"] == "Unknown Product"].shape)
        print(clean_df.duplicated().sum())

        # Load
        print("\n[3/3] Loading data...")
        csv_results = load_data(df=clean_df, csv_path=CSV_FILE)
        postgre_results = load_to_postresql(df=clean_df,
            host="localhost",
            port="5432",
            database="fashion_db",
            username="postgres",
            password="12345",
            table_name="fashion_products")
        gsheets = load_to_google_sheets(
            df=clean_df,
            spreadsheet_id=SPREADSHEET_ID,
            credentials_file=CREDENTIALS_FILE
        )
        if csv_results and postgre_results and gsheets:
          print("\nETL Pipeline completed successfully!")
        else:
            print("\nETL Pipeline failed during loading.")

    except Exception as e:
        print(f"\nMain Pipeline Error: {e}")


if __name__ == "__main__":
    main()