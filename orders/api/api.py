from typing import List
from uuid import UUID

from fastapi.openapi.models import Response
from starlette import status

from orders.app import app
from orders.api.schemas import CreateOrderSchema, GetOrderSchema

order = {
    "id":    'ff0f1355-e821-4178-9567-550dec27a373',
    "status": "delivered",
    "created": 1740493805,
    "updated": 1740493905,
    "order": [
        {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1,
        }
    ]
}


@app.get('/orders',response_model=List[GetOrderSchema])
def get_order():
    return [
        order
    ]


@app.post('/orders', status_code=status.HTTP_201_CREATED,response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    return order


@app.get('/orders/{order_id}',response_model=GetOrderSchema)
def get_order(order_id: UUID):
    return order


@app.put('/orders/{order_id}',response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    return order


@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return


@app.post('/orders/{order_id}/cancel',response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    return order


@app.post('/orders/{order_id}/pay',response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    return order
