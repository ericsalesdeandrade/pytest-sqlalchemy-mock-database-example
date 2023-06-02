from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.database import SessionLocal
from app.models import Order
from app.order import get_order
client = TestClient(app)

# def test_get_order_mock(
#     order_id_fixture, 
#     db_session, 
#     mock_order_object
#     ) -> None:

#     order_id = order_id_fixture
#     db_session.add(mock_order_object)
#     db_session.commit()
#     response = client.get(f"/api/orders/{order_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         'Status': 'Success', 
#         'Order': 
#             {'id': order_id, 
#             'customer_id': '1', 
#             'total_amount': 50, 
#             'updatedAt': None, 
#             'quantity': 2, 
#             'createdAt': '2021-07-03T00:00:00'
#             }
#          }

@pytest.fixture(scope="module")
def mock_get_sqlalchemy_session(mocker):
    mock = mocker.patch(
        "app.database.get_db.query"
    )
    yield mock

def test_get_order_mock(
    mocker,
    ) -> None:
    # Create a mock Order object
    mock_order = mocker.Mock(spec=Order)

    # Mock the query method and its subsequent calls
    mock_query = mocker.Mock(return_value=mock_order)
    mocker.patch('app.order.get_order', mock_query)

    # Call the code under test
    result = get_order(orderId='your_order_id')

    # Assertions or further test code
    assert result == {"Status": "Success", "Order": mock_order}


