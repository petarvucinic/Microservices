from fastapi import FastAPI
# from redis import get_redis_connection, HashModel
from redis_om import get_redis_connection, HashModel
app = FastAPI()

# app.add_middleware

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
    return Product.all_pks()




