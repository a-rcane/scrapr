import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy import DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship

from models.organization import Organization

Base = sa.orm.declarative_base()


class Executives(Base):
    __tablename__ = 'executives'

    executive_id = sa.Column(sa.Uuid, primary_key=True, default=uuid.uuid4)
    executive_name = sa.Column(sa.Text, nullable=False)
    executive_title = sa.Column(sa.Text, nullable=False)
    org_name = sa.Column(sa.Text, ForeignKey(Organization.org_name))

    def __init__(self, executive_name, executive_title, org_name):
        self.executive_name = executive_name
        self.executive_title = executive_title
        self.org_name = org_name

    def __repr__(self):
        return f"{self.executive_id} {self.executive_name} {self.executive_title} {self.org_name}"
