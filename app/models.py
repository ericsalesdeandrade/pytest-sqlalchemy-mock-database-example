from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    # Establishing a relationship with the Orders table
    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    customer_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    # Establishing relationships with other tables
    customer = relationship("Customer", back_populates="orders")
