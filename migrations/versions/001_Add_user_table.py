from sqlalchemy import *
from migrate import *
meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('user_name', String(40)),
    Column('mobile', String(40)),
    Column('password', String(40)),
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    user.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    user.drop()
