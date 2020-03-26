import redis

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import current_app

pool = redis.ConnectionPool()
redis_json = current_app.config.get("REDIS")

if redis_json:
    ts = redis.Redis(host=redis_json.get("host"), port=redis_json.get("port"), db=redis_json.get("db"),
                     connection_pool=pool)
else:
    ts = redis.Redis(connection_pool=pool)  # default params

mysql_json = current_app.config.get("MYSQL")
if not mysql_json:
    raise ConnectionError("config error")

mysql_url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(mysql_json.get("user"), mysql_json.get("password"),
                                                           mysql_json.get("host"), mysql_json.get("port"),
                                                           mysql_json.get("database"))
# 初始化数据库连接:
engine = create_engine(mysql_url, encoding="utf-8", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
