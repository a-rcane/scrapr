import uuid

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker

from models.organization import Organization

Base = sa.orm.declarative_base()


class Funding(Base):
    __tablename__ = 'funding'

    funding_id = sa.Column(sa.Uuid, primary_key=True, default=uuid.uuid4)
    total_funding = sa.Column(sa.Text, nullable=False)
    funding_rounds = sa.Column(sa.BIGINT, nullable=False)
    lead_investors = sa.Column(sa.BIGINT, nullable=False)
    org_name = sa.Column(sa.Text, ForeignKey(Organization.org_name))

    def __init__(self, total_funding, funding_rounds, lead_investors, org_name):
        self.total_funding = total_funding
        self.funding_rounds = funding_rounds
        self.lead_investors = lead_investors
        self.org_name = org_name

    def __repr__(self):
        return f"{self.funding_id} {self.total_funding} {self.funding_rounds} {self.lead_investors}" \
               f" {self.org_name}"
