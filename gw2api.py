import requests
import os
import json

os.environ['HTTP_PROXY'] = 'http://proxy.rockwellcollins.com:9090'
os.environ['HTTPS_PROXY'] =  'http://proxy.rockwellcollins.com:9090'

# access_token = 'CA1D480A-ED83-8841-8118-3141536C18B1AE73DB4D-A078-4DD7-9E86-5AB4C29EE7CD'

def get_account_name(access_token):
    payload = {'access_token' : access_token }
    response = requests.get('https://api.guildwars2.com/v2/account', params=payload)
    json_response = response.json()
    print(f'The account name is: {json_response['name']}')

if __name__ == '__main__':
    get_account_name()