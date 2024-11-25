from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    products_id: str = Field(description="The ID of the product to order")
    quantity: int = Field(description="The quantity of the product to order")


class Order(BaseModel):
    products: list[OrderItem] = Field(description="List of the items to order")
