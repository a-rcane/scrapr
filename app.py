from apis import org_api, fund_api, exec_api
from configs.config import settings
from base.utils import create_app

app = create_app()
app.config['SECRET_KEY'] = settings.get('secret_key')


@app.route('/')
def ping():
    return 'ping!'


# list organizations
app.add_url_rule('/organizations', view_func=org_api.list_organization_names, methods=['GET'])

# add organization to db
app.add_url_rule('/organizations/add/<org_name>', view_func=org_api.add_org_info, methods=['POST'])

# add organization fund info to db
app.add_url_rule('/organizations/add/funding_info/<org_name>', view_func=fund_api.add_org_fund_info, methods=['POST'])

# add organization exec info to db
app.add_url_rule('/organizations/add/executives_info/<org_name>', view_func=exec_api.add_org_exec_info,
                 methods=['POST'])

# search for organization by name
app.add_url_rule('/organizations/search/<org_name>',
                 view_func=org_api.find_organization, methods=['GET'])

# find funding info of org by org name
app.add_url_rule('/organization/funding_info/<org_name>',
                 view_func=fund_api.list_funding_names, methods=['GET'])

# find executive info of org by org name
app.add_url_rule('/organization/executive_info/<org_name>',
                 view_func=exec_api.list_executive_names, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
