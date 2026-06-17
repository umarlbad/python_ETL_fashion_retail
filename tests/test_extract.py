from unittest.mock import patch, Mock
from utils.extract import scraping_data

@patch("utils.extract.requests.get")
def test_scraping_data(mock_get):
    html = """
    <div class="collection-card">
        <div class="product-details">
            <h3 class="product-title">
                Test Shirt
            </h3>
            <span class="price">
                $50
            </span>
            <p>
                Rating: ⭐ 4.8 / 5
            </p>
            <p>
                3 Colors
            </p>
            <p>
                Size: XL
            </p>
            <p>
                Gender: Men
            </p>
        </div>
    </div>
    """
    mock_response = Mock()
    mock_response.text = html
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    df = scraping_data(
        "https://dummy.com")
    assert len(df) > 0
    assert "title" in df.columns
    assert "price" in df.columns

@patch("utils.extract.requests.get")
def test_scraping_request_error(mock_get):
    mock_get.side_effect = Exception(
        "Connection Error")
    df = scraping_data("https://dummy.com")
    assert df is not None