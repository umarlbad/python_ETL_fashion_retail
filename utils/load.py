import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def load_to_csv(df:pd.DataFrame, csv_path:str)->bool:
  """save dataFrame to csv"""
  try:
    df.to_csv(csv_path, index=False)
    print(f"Data saved to csv: {csv_path}")
    return True
  
  except Exception as e:
    print(f"CSV load Error: {e}")
    return False
  
def load_to_postresql(df:pd.DataFrame, host:str, port:str, database:str, username:str, password:str, table_name:str) ->bool:
  try:
    connect_string= (
      f"postgresql://{username}:{password}"
      f"@{host}:{port}/{database}"
    )
    engine = create_engine(connect_string)
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print(f"Data saved to PostgreSQL table: {table_name}")
    return True
  except Exception as e:
    print(f"PostgreSQL Load Error: \n{e}")
    return False
  
def load_to_google_sheets(df: pd.DataFrame, spreadsheet_id: str, credentials_file: str, sheet_name: str = "Sheet1") -> bool:
    """Save DataFrame to Google Sheets."""
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        credentials = (Credentials.from_service_account_file(
                credentials_file,scopes=scopes))
        service = build("sheets","v4",credentials=credentials)
        df = df.copy()
        if "timestamp" in df.columns:
            df['timestamp'] = (df['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S"))
        values = [df.columns.tolist()] + df.values.tolist()
        body = {"values": values}
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body=body).execute()
        print("✓ Data saved to Google Sheets")
        return True

    except Exception as e:
        print(f"Google Sheets Load Error: {e}")
        return False

def load_data(df: pd.DataFrame,csv_path:str) -> bool:
    """Main load pipeline.Required for Basic submission."""
    try:
        if df.empty:
          raise ValueError("DataFrame is empty. Nothing to load.")
        else:
          success = load_to_csv(df=df, csv_path=csv_path)
          return success
    except Exception as e:
      print(f"Load Pipeline Error: {e}")
      return False
