import app.schemas as schemas
import app.models as models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from app.database import get_db

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_orders(
    db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""
):
    skip = (page - 1) * limit

    orders = (
        db.query(models.Order)
        .limit(limit)
        .offset(skip)
        .all()
    )
    return {"Status": "Success", "Results": len(orders), "Orders": orders}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_order(payload: schemas.OrderBaseSchema, db: Session = Depends(get_db)):
    new_order = models.Order(**payload.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"Status": "Success", "Order": new_order}


@router.patch("/{orderId}", status_code=status.HTTP_202_ACCEPTED)
def update_order(
    orderId: str, payload: schemas.OrderBaseSchema, db: Session = Depends(get_db)
):
    order_query = db.query(models.Order).filter(models.Order.id == orderId)
    db_order = order_query.first()

    if not db_order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Order with this id: {orderId} found",
        )
    update_data = payload.dict(exclude_unset=True)
    order_query.filter(models.Order.id == orderId).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_order)
    return {"Status": "Success", "Order": db_order}


@router.get("/{orderId}", status_code=status.HTTP_200_OK)
def get_order(orderId: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == orderId).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Order with this id: `{orderId}` found",
        )
    return {"Status": "Success", "Order": order}


@router.delete("/{orderId}", status_code=status.HTTP_200_OK)
def delete_order(orderId: str, db: Session = Depends(get_db)):
    order_query = db.query(models.Order).filter(models.Order.id == orderId)
    order = order_query.first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No order with this id: {orderId} found",
        )
    order_query.delete(synchronize_session=False)
    db.commit()
    return {"Status": "Success", "Message": "Order deleted successfully"}
