from base.db_ops.db_ops import DBOps
from configs.config import settings
from models.executives import Executives
from operational_units.executives_scraper import ExecutivesScraper


class ExecOperations(DBOps):
    def __init__(self, connection_string=settings.DB_URI):
        super().__init__(connection_string)

    def list_executives_info(self, org_name):
        try:
            with self.create_session() as session:
                res = session.query(Executives).filter(Executives.org_name == org_name).all()
                if res is not None:
                    data = []
                    for r in res:
                        data.append({
                            'executive_id': r.executive_id,
                            'org_name': r.org_name,
                            'executive_name': r.executive_name,
                            'executive_title': r.executive_title
                        }
                        )
                    return data
                else:
                    return 'no executive info found'
        except Exception as e:
            print(e)

    # use exec scraper data
    def add_organization_exec_info(self, organization_name):
        try:
            with self.create_session() as session:
                p = session.query(Executives).filter(Executives.org_name == organization_name).all()
            if p is not None and len(p) > 0:
                print(f'{organization_name} executive data already exists')
                ret = []
                for val in p:
                    ret.append({
                            'executive_id': val.executive_id,
                            'executive_name': val.executive_name,
                            'executive_title': val.executive_title,
                        })
                return ret
            else:
                return ExecutivesScraper().add_exec_data(organization_name)
        except Exception as e:
            print(e)
