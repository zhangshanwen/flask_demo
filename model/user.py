from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INT

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(INT(), primary_key=True)
    user_name = Column(String(), )
    mobile = Column(String(), )
    password = Column(String(), )
