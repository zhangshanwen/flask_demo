from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    note = Column('note', String(128),comment="测试")
    note.create(user)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass


