import time

from base.db_ops.db_ops import DBOps
from models.executives import Executives
from operational_units.scraper import BaseScraper


class ExecutivesScraper(BaseScraper):

    def executives_scrape(self, org_name):
        exec_url = f'https://www.crunchbase.com/organization/{org_name}/people'
        soup = self.return_soup(exec_url)

        names = soup.select('.fields a.accent')
        roles = soup.select('.fields span.field-type-text_short')
        en_roles = soup.select('.fields span.field-type-enum')

        nm = []
        rl = []

        for n in names:
            nm.append(n.text.strip())
        for r in roles:
            rl.append(r.text.strip())
        for e_r in en_roles:
            rl.append(e_r.text.strip())

        data_dict = dict(zip(nm, rl))
        print('info: ', data_dict)
        return data_dict

    def add_exec_data(self, org_name):
        with DBOps().create_session() as s:
            p = s.query(Executives).filter(Executives.org_name == org_name).all()
        print(len(p))
        if len(p) == 0:
            data_dict = self.executives_scrape(org_name)
            if len(data_dict) > 0:
                try:
                    with DBOps().create_session() as s:
                        for k in data_dict:
                            execs = Executives(k, data_dict[k], org_name)
                            s.add(execs)
                            s.commit()
                        return data_dict
                except Exception as e:
                    print(e)
            else:
                print("Scraper didn't work")
        else:
            print('Executive data exists for this organization')


if __name__ == '__main__':
    start = time.time()

    ExecutivesScraper().add_exec_data('flexport')

    end = time.time()
    print(str(end - start) + " s")
