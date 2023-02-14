from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']

)

redis = get_redis_connection(
    host="redis-13116.c240.us-east-1-3.ec2.cloud.redislabs.com",
    port=13116,
    password="giPDndyJ2Y0w7j0IMLBbCyV09ETqnuZn",
    decode_responses=True
)

class Product():
    name:str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()

@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)

@app.delete("/products/{pk}")
def delete(pk: str):
    return product.delete(pk)
