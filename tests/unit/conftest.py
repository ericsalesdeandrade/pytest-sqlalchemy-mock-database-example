from datetime import datetime
import pytest
import uuid
from app.database import Base, engine, SessionLocal
from app.models import Order


@pytest.fixture(scope="module")
def order_id_fixture():
    order_id = str(uuid.uuid4())
    return order_id
    

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()



@pytest.fixture(scope="module")
def mock_order_object(order_id_fixture):
    order = Order(
        id=order_id_fixture,
        customer_id="1", 
        quantity=2, 
        total_amount=50,
        createdAt=datetime(2021, 7, 3, 0, 0, 0, 0),
        updatedAt=None
        )
    return order


