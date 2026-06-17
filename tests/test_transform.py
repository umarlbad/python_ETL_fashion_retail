import pandas as pd

from utils.transform import (clean_price, clean_rating, clean_colors, clean_size,
    clean_gender, remove_invalid_rows, convert_data_types, transform_data)


def test_clean_price():
    assert clean_price("$50") == 800000.0
def test_clean_price_invalid():
    assert clean_price("Price Unavailable") is None
def test_clean_rating():
    assert clean_rating("Rating: ⭐ 4.8 / 5") == 4.8
def test_clean_rating_invalid():
    assert clean_rating("Rating: ⭐ Invalid Rating / 5") is None
def test_clean_colors():
    assert clean_colors("3 Colors") == 3
def test_clean_size():
    assert clean_size("Size: XL") == "XL"
def test_clean_gender():
    assert clean_gender("Gender: Men") == "Men"
def test_remove_invalid_rows():
    df = pd.DataFrame({"title": ["Unknown Product", "Nike Shirt"]})
    result = remove_invalid_rows(df)
    assert len(result) == 1
    assert result.iloc[0]["title"] == "Nike Shirt"
def test_convert_data_types():
    df = pd.DataFrame({
        "title": ["Nike Shirt"], "price": [800000], "rating": [4.8],
        "colors": [3], "size": ["XL"], "gender": ["Men"]})
    result = convert_data_types(df)
    assert str(result["price"].dtype) == "float64"
    assert str(result["rating"].dtype) == "float64"
    assert str(result["colors"].dtype) == "int64"

def test_transform_data():
    df = pd.DataFrame({"title": ["Nike Shirt", "Unknown Product"],"price": ["$50", "Price Unavailable"], "rating": ["Rating: ⭐ 4.8 / 5", "Rating: ⭐ Invalid Rating / 5"],
                        "colors": ["3 Colors", "2 Colors"], "size": ["Size: XL","Size: L"], "gender": ["Gender: Men", "Gender: Women"]})
    result = transform_data(df)
    assert len(result) == 1
    assert result.iloc[0]["title"] == "Nike Shirt"
    assert result.iloc[0]["price"] == 800000.0
    assert result.iloc[0]["rating"] == 4.8
    assert result.iloc[0]["colors"] == 3

def test_clean_price_none():
    assert clean_price(None) is None
def test_clean_rating_none():
    assert clean_rating(None) is None
def test_clean_colors_none():
    assert clean_colors(None) is None
def test_clean_size_none():
    assert clean_size(None) is None
def test_clean_gender_none():
    assert clean_gender(None) is None
def test_clean_colors_invalid():
    assert clean_colors("abc") is None