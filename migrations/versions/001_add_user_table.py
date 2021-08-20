import time

from sqlalchemy import Table, Column, Integer, String, MetaData

from tools.code import generate_md5
from manage import config

meta = MetaData()

user = Table(
    "user", meta,
    Column('id', Integer, primary_key=True),
    Column('user_name', String(40)),
    Column('mobile', String(40)),
    Column('password', String(40)),
    Column('created_time', Integer),
    Column('updated_time', Integer),
    Column('last_login_time', Integer),

)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    user.create()
    res = user.insert().values(user_name=config.get("DEFAULT_USERNAME"), mobile=config.get("DEFAULT_MOBILE"),
                               password=generate_md5(config.get("SALT") + config.get("DEFAULT_PASSWORD")),
                               created_time=int(time.time()))
    migrate_engine.execute(res)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    user.drop()
