from base.db_ops.db_ops import DBOps
from base.db_ops.exec_ops import ExecOperations
from base.db_ops.fund_ops import FundOperations
from configs.config import settings
from models.organization import Organization
from operational_units.executives_scraper import ExecutivesScraper
from operational_units.funding_scraper import FundingScraper


class OrgOperations(DBOps):
    def __init__(self, connection_string=settings.DB_URI):
        super().__init__(connection_string)

    def list_organizations(self):
        try:
            with self.create_session() as session:
                res = session.query(Organization).all()
            if res is not None and len(res) > 0:
                ret_val = []
                for r in res:
                    ret_val.append(
                        {
                            'org_id': r.org_id,
                            'org_name': r.org_name,
                        })
                return ret_val
            else:
                return None
        except Exception as e:
            print(e)

    def add_organization(self, org_name):
        try:
            if org_name is not None:
                org = Organization(org_name)
                organization_name = org.org_name
                with self.create_session() as session:
                    p = session.query(Organization).filter(Organization.org_name == organization_name).first()
                    if p is None:
                        session.add(org)
                        session.commit()
                        return {
                                'org_id': org.org_id,
                                'org_name': org.org_name
                               }
                    else:
                        return f"{org_name} already exists"
        except Exception as e:
            print(e)

    def add_organization_info(self, organization_name):
        try:
            with self.create_session() as session:
                p = session.query(Organization).filter(Organization.org_name == organization_name).first()
                if p is None:
                    OrgOperations().add_organization(organization_name)
                else:
                    print(f'{organization_name} already exists')

            return {'org_name': organization_name}
        except Exception as e:
            print(e)

    @staticmethod
    def find_organization_by_name(organization_name):
        try:
            ex_ops = ExecOperations()
            fnd_ops = FundOperations()
            return {
                    'org_name': organization_name,
                    'executive_info': ex_ops.list_executives_info(organization_name),
                    'funding_info': fnd_ops.list_funding_info(organization_name)
                }
        except Exception as e:
            print(e)
