from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def mock_db(mocker):

    # Mock the behavior of the database connection methods
    mocker.execute.return_value = "Mock result"
    mocker.fetch_all.return_value = [("Mock data 1",), ("Mock data 2",)]

    # Patch the get_db dependency to return the mock connection
    mocker.patch("main.get_db", return_value=mocker)

    yield mocker

def test_example(mock_db):
    # Make requests to your FastAPI application using the TestClient
    client = TestClient(app)
    response = client.get("/orders")

    assert response.status_code == 200
    print(response.json())
    # assert response.json() == {"result": "Mock result"}

    # Verify that the database connection methods were called as expected
    mock_db.execute.assert_called_once_with("SELECT * FROM table")
    mock_db.fetch_all.assert_called_once()