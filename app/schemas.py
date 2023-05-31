from datetime import datetime
from typing import List
from pydantic import BaseModel

class OrderBaseSchema(BaseModel):
    id: str | None = None
    customer_id: str
    quantity: str
    total_amount: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


# class ListOrderResponse(BaseModel):
#     status: str
#     results: int
#     users: List[OrderBaseSchema]
