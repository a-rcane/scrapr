import os
import requests
from fake_useragent import UserAgent

from apis import org_api, fund_api, exec_api
from configs.config import settings
from base.utils import create_app
from operational_units.rotating_proxies import check_proxies

app = create_app()
app.config['SECRET_KEY'] = settings.get('secret_key')


@app.route('/')
def ping():
    return 'ping!'


@app.route('/run-all', methods=['POST'])
def run_all():
    org_list = ['flexport', 'google', 'perplexity-ai', 'limechat', 'ShipMonk', 'Cargomatic', 'Fleet',
                'Bungii', 'Percepta', 'WideSense']
    abs_path = os.path.dirname(__file__)
    file_path = os.path.join(abs_path, 'apis.txt')
    apis_list = open(file_path, "r").read().strip().split("\n")
    base = 'https://94de-49-36-183-190.ngrok-free.app'
    for org in org_list:
        for api in apis_list:
            proxy_val = check_proxies()
            ua = UserAgent()
            user_agent = ua.random
            print('user_agent: ', user_agent)
            print('proxy: ', proxy_val)
            header = {
                'User-Agent': user_agent,
                'Referer': 'https://www.google.com/'
            }
            url = base + api + f'{org}'
            print(url)
            requests.post(url, proxies={"http": f"http://{proxy_val}"}, headers=header)

    return 'ping!'


# list organizations
app.add_url_rule('/organizations', view_func=org_api.list_organization_names, methods=['GET'])

# add organization to db
app.add_url_rule('/organizations/add/<org_name>', view_func=org_api.add_org_info, methods=['POST'])

# add organization fund info to db
app.add_url_rule('/organizations/add/funding_info/<org_name>', view_func=fund_api.add_org_fund_info, methods=['POST'])

# add organization exec info to db
app.add_url_rule('/organizations/add/executive_info/<org_name>', view_func=exec_api.add_org_exec_info,
                 methods=['POST'])

# search for organization by name
app.add_url_rule('/organizations/search/<org_name>',
                 view_func=org_api.find_organization, methods=['GET'])

# find funding info of org by org name
app.add_url_rule('/organizations/funding_info/<org_name>',
                 view_func=fund_api.list_funding_names, methods=['GET'])

# find executive info of org by org name
app.add_url_rule('/organizations/executive_info/<org_name>',
                 view_func=exec_api.list_executive_names, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
