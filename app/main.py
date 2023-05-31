from app import models, order
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
# from models import Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Route for Orders
app.include_router(order.router, tags=["Orders"], prefix="/api/orders")

@app.get("/api/healthchecker")
def root():
    return {"message": "The API is Working!!"}
