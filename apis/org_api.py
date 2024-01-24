from base.db_ops.org_ops import OrgOperations

org = OrgOperations()


def list_organization_names():
    try:
        res = org.list_organizations()
        if res is not None:
            return res
        else:
            return 'No organizations found'
    except Exception as e:
        print(e)


def find_organization(org_name):
    try:
        res = org.find_organization_by_name(org_name)
        if res is not None:
            return res
        else:
            return 'Organization not found'
    except Exception as e:
        print(e)


def add_org_info(org_name):
    try:
        res = org.add_organization_info(org_name)
        if res is not None:
            return res
        else:
            return 'Organization not found'
    except Exception as e:
        print(e)
