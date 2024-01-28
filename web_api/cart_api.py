from http import HTTPStatus as hs
from fastapi import APIRouter, HTTPException
from models.cart_model import DeliveryFeeRequest, DeliveryFeeResponse
from services.delivery_fee_service import DeliveryFeeCalculator

router = APIRouter(prefix="/cart")


@router.post("/calculate-delivery-fee", response_model=DeliveryFeeResponse)
async def calculate_delivery_fee(payload: DeliveryFeeRequest):
    try:
        delivery_fee = DeliveryFeeCalculator(
            payload.cart_value,
            payload.delivery_distance,
            payload.number_of_items,
            payload.time,
        ).calculate_fee()
        return {"delivery_fee": delivery_fee}
    except ValueError as e:
        raise HTTPException(hs.BAD_REQUEST, detail=str(e)) from e
