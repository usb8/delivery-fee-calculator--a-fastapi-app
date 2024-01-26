from http import HTTPStatus as hs
from fastapi import APIRouter, HTTPException
from models.cart_model import DeliveryFeeRequest, DeliveryFeeResponse

router = APIRouter(prefix="/cart")

@router.post("/calculate-delivery-fee", response_model=DeliveryFeeResponse)
async def calculate_delivery_fee(payload: DeliveryFeeRequest):
    try:
        delivery_fee = calculate_fee(
            payload.cart_value,
            payload.delivery_distance,
            payload.number_of_items,
            payload.time,
        )
        return {"delivery_fee": delivery_fee}
    except ValueError as e:
        raise HTTPException(hs.BAD_REQUEST, detail=str(e)) from e


def calculate_fee(
    cart_value: int, delivery_distance: int, number_of_items: int, time: str
) -> int:
    return 999
