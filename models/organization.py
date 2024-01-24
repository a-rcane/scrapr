import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy import DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = sa.orm.declarative_base()


class Organization(Base):
    __tablename__ = 'organization'

    org_id = sa.Column(sa.Uuid, primary_key=True, default=uuid.uuid4)
    org_name = sa.Column(sa.Text, nullable=False)

    def __init__(self, org_name):
        self.org_name = org_name

    def __repr__(self):
        return f"{self.org_id} {self.org_name}"
