from base.db_ops.fund_ops import FundOperations

fund = FundOperations()


def list_funding_names(org_name):
    try:
        res = fund.list_funding_info(org_name)
        if res is not None:
            return res
        else:
            return 'No funding info'
    except Exception as e:
        print(e)


def add_org_fund_info(org_name):
    try:
        res = fund.add_organization_fund_info(org_name)
        if res is not None:
            return res
        else:
            return 'Organization not found'
    except Exception as e:
        print(e)
