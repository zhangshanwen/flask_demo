from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    email = Column('email', String(128))
    email.create(user)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass