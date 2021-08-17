import time
from sqlalchemy import Column, String, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = "user"

    # 表的结构:
    id = Column(INT(), primary_key=True)
    user_name = Column(String(), )
    mobile = Column(String(), )
    password = Column(String(), )
    last_login_time = Column(INT(), default=0)
    created_time = Column(INT(), default=int(time.time()))
    updated_time = Column(INT(), default=int(time.time()), onupdate=int(time.time()))
