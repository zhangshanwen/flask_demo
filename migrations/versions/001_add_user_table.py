from sqlalchemy import Table, Column, Integer, String, MetaData

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


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    user.drop()
