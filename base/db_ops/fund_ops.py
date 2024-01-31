from base.db_ops.db_ops import DBOps
from configs.config import settings
from models.funding import Funding
from operational_units.funding_scraper import FundingScraper


class FundOperations(DBOps):
    def __init__(self, connection_string=settings.DB_URI):
        super().__init__(connection_string)

    def list_funding_info(self, org_name):
        try:
            with self.create_session() as session:
                res = session.query(Funding).filter(Funding.org_name == org_name).all()
                if res is not None:
                    data = []
                    for r in res:
                        data.append({
                                'funding_id': r.funding_id,
                                'total_funding': r.total_funding,
                                'funding_rounds': r.funding_rounds,
                                'lead_investors': r.lead_investors,
                               }
                        )
                    return data
                else:
                    return 'no funding info found'
        except Exception as e:
            print(e)

    # use funding scraper data
    def add_organization_fund_info(self, organization_name):
        try:
            with self.create_session() as session:
                p = session.query(Funding).filter(Funding.org_name == organization_name).first()
            if p is not None and len(p) > 0:
                print(f'{organization_name} fund data already exists')
                return {
                    'funding_id': p.funding_id,
                    'total_funding': p.total_funding,
                    'funding_rounds': p.funding_rounds,
                    'lead_investors': p.lead_investors,
                }
            else:
                return FundingScraper().add_fund_data(organization_name)
        except Exception as e:
            print(e)
