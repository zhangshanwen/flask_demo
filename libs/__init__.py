import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pool = redis.ConnectionPool()
ts = redis.Redis(connection_pool=pool)


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
