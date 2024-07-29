
import requests

def get_sql_app(app_name):
    url = "http://180.184.80.35:6688/aiquant-mark/page-data/queryApp"
    param = {'appName': app_name}
    response = requests.get(url, params=param)
    return response.json()

def wake_function_5(app_name):
    response = get_sql_app(app_name)
    if response['code'] == '00000000' and response['data']:
        return True
    return False
