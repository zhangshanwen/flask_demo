import redis

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import current_app
from tools.log import AppLog

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

AppLog.init_log(current_app.config.get("LOG_PATH"))
# 初始化数据库连接:
engine = create_engine(mysql_json.get("url"), encoding="utf-8", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
db = DBSession()
