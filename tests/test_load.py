import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import (
    load_to_csv,
    load_data, load_to_postresql, load_to_google_sheets)

def test_load_to_csv(tmp_path):
    df = pd.DataFrame({
        "title": ["Shirt"],
        "price": [800000]})
    file_path = tmp_path / "fashion_products_test.csv"
    result = load_to_csv(
        df, str(file_path))
    assert result is True
    assert file_path.exists()

def test_load_data():
    df = pd.DataFrame({
        "title": ["Shirt"],
        "price": [800000]})
    result = load_data(df, "fashion_products_test.csv")
    assert result is True

def test_load_data_empty():
    df = pd.DataFrame()
    result = load_data(df, "fashion_products_test.csv")
    assert result is False

@patch("utils.load.create_engine")
def test_load_to_postgresql(mock_engine):
    df = pd.DataFrame({
        "title": ["Shirt"]
    })
    result = load_to_postresql(
        df=df,
        host="localhost",
        port="5432",
        database="fashion_db",
        username="postgres",
        password="12345",
        table_name="fashion_products_dummy"
    )
    assert result is True

@patch("utils.load.create_engine")
def test_load_to_postgresql_error(mock_engine):
    mock_engine.side_effect = Exception(
        "Database Error"
    )
    df = pd.DataFrame({
        "title": ["Shirt"]
    })
    result = load_to_postresql(
        df=df,
        host="localhost",
        port="5432",
        database="fashion_db",
        username="postgres",
        password="12345",
        table_name="fashion_products_dummy"
    )
    assert result is False

@patch("utils.load.build")
@patch("utils.load.Credentials")
def test_google_sheet_success(
    mock_credentials,
    mock_build
):
    df = pd.DataFrame({
        "title": ["Shirt"]
    })
    mock_service = MagicMock()
    mock_build.return_value = mock_service
    result = load_to_google_sheets(
        df=df,
        spreadsheet_id="dummy",
        credentials_file="dummy.json"
    )
    assert result is True

@patch("utils.load.Credentials")
def test_google_sheet_error(
    mock_credentials
):
    mock_credentials.from_service_account_file.side_effect = Exception(
        "Google Error"
    )
    df = pd.DataFrame({
        "title": ["Shirt"]
    })
    result = load_to_google_sheets(
        df=df,
        spreadsheet_id="dummy",
        credentials_file="dummy.json"
    )
    assert result is False