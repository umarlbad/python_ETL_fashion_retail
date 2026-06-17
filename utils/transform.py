import re
import pandas as pd
USD_TO_IDR = 16000
# Clean All Features Selected
def clean_price(price):
  """
  Converting: $50.00 => 800000.0
  Price Unavailable -> None
  """
  try:
    if pd.isna(price):
      return None
    
    price = str(price).strip()
    if (price == "" or "Unavailable" in price or "Invalid" in price):
      return None
    
    value_kurs = float(price.replace("$", ""))
    return value_kurs * USD_TO_IDR
  
  except Exception:
    return None

def clean_rating(rating):
  """Converting: 4.8 / 5 -> 4.8"""
  try:
    if pd.isna(rating):
      return None
    rating = str(rating).strip()
    if "Invalid Rating" in rating:
      return None
    match = re.search(r"(\d+\.?\d*)", rating)
    if match:
      return float(match.group(1))
    
    return None
  
  except Exception:
    return None

def clean_colors(colors):
  """Converting: 3 Colors -> 3"""
  try:
    if pd.isna(colors):
      return None
    
    colors = str(colors).strip()
    match = re.search(r"(\d+)", colors)
    if match:
      return int(match.group(1))
    
    return None
  
  except Exception:
    return None

def clean_size(size):
  """Converting: Size: XL -> XL"""
  try:
    if pd.isna(size):
      return None
    
    size = str(size)
    return (size.replace("Size:", "").strip())
  except Exception:
    return None

def clean_gender(gender):
    """
    Convert:
    Gender: Men -> Men
    """

    try:
        if pd.isna(gender):
            return None

        gender = str(gender)

        return (
            gender
            .replace("Gender:", "")
            .strip()
        )

    except Exception:
        return None

def remove_invalid_rows(df):
    """
    Remove invalid products
    """
    try:
        invalid_titles = ["Unknown Product"]
        df = df[~df["title"].isin(invalid_titles)]
        return df
    except Exception:
        return pd.DataFrame()

def convert_data_types(df):
    """
    Ensure correct datatype
    """
    try:
        df["title"] = df["title"].astype(str)
        df["price"] = df["price"].astype(float)
        df["rating"] = df["rating"].astype(float)
        df["colors"] = df["colors"].astype(int)
        df["size"] = df["size"].astype(str)
        df["gender"] = df["gender"].astype(str)
        return df

    except Exception:
        return pd.DataFrame()

def transform_data(df):
    """
    Main transformation pipeline
    """

    try:
        # Cleaning columns
        df["price"] = df["price"].apply(clean_price)
        df["rating"] = df["rating"].apply(clean_rating)
        df["colors"] = df["colors"].apply(clean_colors)
        df["size"] = df["size"].apply(clean_size)
        df["gender"] = df["gender"].apply(clean_gender)
        # Remove invalid product
        df = remove_invalid_rows(df)
        # Remove null
        df = df.dropna()
        # Remove duplicate
        df = df.drop_duplicates()
        # Convert datatype
        df = convert_data_types(df)
        return df
    except Exception as e:
        print(f"Transform Error: {e}")
        return pd.DataFrame()
