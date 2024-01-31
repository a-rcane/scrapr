import time

import requests

from base.db_ops.db_ops import DBOps
from models.funding import Funding
from operational_units.scraper import BaseScraper


class FundingScraper(BaseScraper):
    def funding_scrape(self, org_name):
        cache_url = self.cache_url
        exec_url = cache_url + f'crunchbase.com/organization/{org_name}/company_financials'

        if requests.get(exec_url).status_code != 200:
            exec_url = f'https://www.crunchbase.com/organization/{org_name}/company_financials'

        print(exec_url)
        soup = self.return_soup(exec_url)

        data_dict = {}

        data_dict['funding_rounds'] = None
        data_dict['lead_investors'] = None

        for i in range(1, 7):
            checker = f'.spacer:nth-of-type({i}) a span.wrappable-label-with-info'
            if soup.select_one(checker).text.strip() == 'Lead Investors':
                lead_investor_element = soup.select_one(f'.spacer:nth-of-type({i}) a .component--field-formatter')
                data_dict['funding_rounds'] = lead_investor_element.text
            if soup.select_one(checker).text.strip() == 'Funding Rounds':
                funding_rounds_element = soup.select_one(f'.spacer:nth-of-type({i}) a .component--field-formatter')
                data_dict['lead_investors'] = funding_rounds_element.text

        data_dict['total_funding'] = soup.select_one('span.field-type-money')['title']

        print(data_dict)
        return data_dict

    def add_fund_data(self, org_name):
        data_dict = self.funding_scrape(org_name)
        if len(data_dict) > 0:
            try:
                with DBOps().create_session() as s:
                    fund = Funding(data_dict['total_funding'], data_dict['funding_rounds'],
                                   data_dict['lead_investors'], org_name)
                    s.add(fund)
                    s.commit()
                    return data_dict
            except Exception as e:
                print(e)
        else:
            print("Scraper didn't work")


if __name__ == '__main__':
    start = time.time()
    # FundingScraper().funding_scrape('flexport')
    # FundingScraper().add_fund_data('flexport')

    end = time.time()
    print(str(end - start) + " s")
