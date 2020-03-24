import redis

pool = redis.ConnectionPool()
ts = redis.Redis(connection_pool=pool)
