from fastapi.testclient import TestClient
from app.main import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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

@pytest.fixture
def mock_session(request, mocker):
    session = mocker.create_autospec(Session)
    # Customize the session behavior if needed
    return session

def test_get_order_mock(mocker, order_id_fixture) -> None:
    order_id = order_id_fixture
    mock_response = {
        'Status': 'Success', 
        'Order': 
            {'id': order_id, 
            'customer_id': '1', 
            'total_amount': 50, 
            'updatedAt': None, 
            'quantity': 2, 
            'createdAt': '2021-07-03T00:00:00'
            }
         }
    mocker.patch(
        "app.database.Base.create_all", return_value=None
    )
    mocker.patch(
        "app.database.SessionLocal", return_value=None
    )
    mocker.patch(
        "app.main.app.get", return_value=mock_response
    )
    response = client.get(f"/api/orders/{order_id}")
    assert response.status_code == 200
    assert response.json() == mock_response
