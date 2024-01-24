import time

from base.db_ops.db_ops import DBOps
from models.funding import Funding
from operational_units.scraper import BaseScraper


class FundingScraper(BaseScraper):

    def funding_scrape(self, org_name):
        exec_url = f'https://www.crunchbase.com/organization/{org_name}/company_financials'
        soup = self.return_soup(exec_url)

        data_dict = {}

        if soup.select_one('.spacer:nth-of-type(6) a .component--field-formatter') is not None:
            lead_investor_element = soup.select_one('.spacer:nth-of-type(6) a .component--field-formatter')
        else:
            lead_investor_element = soup.select_one('.spacer:nth-of-type(3) a .component--field-formatter')

        if soup.select_one('.spacer:nth-of-type(4) a .component--field-formatter') is not None:
            funding_rounds_element = soup.select_one('.spacer:nth-of-type(4) a .component--field-formatter')
        else:
            funding_rounds_element = soup.select_one('.spacer:nth-of-type(1) a .component--field-formatter')

        lead_investor = lead_investor_element.text if lead_investor_element else None
        funding_rounds = funding_rounds_element.text if funding_rounds_element else None

        data_dict['total_funding'] = soup.select_one('span.field-type-money')['title']
        data_dict['lead_investors'] = lead_investor
        data_dict['funding_rounds'] = funding_rounds

        print(data_dict)
        return data_dict

    def add_fund_data(self, org_name):
        data_dict = self.funding_scrape(org_name)
        if len(data_dict) > 0:
            dbops = DBOps()
            try:
                with dbops.create_session() as s:
                    if s.query(Funding).filter(Funding.org_name == org_name).all() is None:
                        fund = Funding(data_dict['total_funding'], data_dict['funding_rounds'],
                                       data_dict['lead_investors'], org_name)
                        s.add(fund)
                        s.commit()
                    else:
                        print('Funding data exists for this organization')
                    return data_dict
            except Exception as e:
                print(e)
        else:
            print("Scraper didn't work")


if __name__ == '__main__':
    start = time.time()

    FundingScraper().add_fund_data('flexport')

    end = time.time()
    print(str(end - start) + " s")
