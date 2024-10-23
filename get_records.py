from seed import Author, Quote
import redis
from redis_lru import RedisLRU

# Redis server configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
CACHE_MAXSIZE = 100  # Maximum number of items to store in the cache

# Create a Redis client
try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    # Test the connection
    redis_client.ping()
    print("Connected to Redis successfully.")
except redis.exceptions.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")
    exit(1)

# Initialize RedisLRU with the Redis client and maximum cache size
cache = RedisLRU(redis_client)

@cache
def get_all_author_quotes(name):
    print('dfsdf')
    author = Author.objects(fullname=name).first()
    if not author:
        print(f'No author found with such name "{name}"')
        return
    quotes = Quote.objects(author=author)
    result = [quote.quote for quote in quotes]
    return result

@cache
def get_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    result = [quote.quote for quote in quotes]
    return result

@cache
def get_quotes_by_all_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    result = [quote.quote for quote in quotes]
    return result
