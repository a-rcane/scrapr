from base.db_ops.exec_ops import ExecOperations

execs = ExecOperations()


def list_executive_names(org_name):
    try:
        res = execs.list_executives_info(org_name)
        if res is not None:
            return res
        else:
            return 'No executive info'
    except Exception as e:
        print(e)


def add_org_exec_info(org_name):
    try:
        res = execs.add_organization_fund_info(org_name)
        if res is not None:
            return res
        else:
            return 'Organization not found'
    except Exception as e:
        print(e)
