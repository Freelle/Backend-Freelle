import redis
import os

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_HOST_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_HOST_PORT,
    db=REDIS_DB,
    decode_responses=True,
)