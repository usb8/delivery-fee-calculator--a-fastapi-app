from pydantic import BaseModel, Field


class DeliveryFeeRequest(BaseModel):
    cart_value: int = Field(
        ..., ge=0, description="Value of the shopping cart in cents."
    )
    delivery_distance: int = Field(
        ...,
        ge=0,
        description="The distance between the store and customer’s location in meters.",
    )
    number_of_items: int = Field(
        ..., ge=0, description="The number of items in the customer's shopping cart."
    )
    time: str = Field(
        ...,
        description="Order time in UTC in ISO format.",
        examples=["2024-01-15T13:00:00Z"],
    )


class DeliveryFeeResponse(BaseModel):
    delivery_fee: int = Field(
        ..., ge=0, le=1500, description="Calculated delivery fee in cents."
    )
