import os
import requests

PATROWL_ENDPOINT = os.environ.get('PATROWL_ENDPOINT', 'http://my.patrowl.io:8000')
PATROWL_AUTH_TOKEN = os.environ.get('PATROWL_AUTH_TOKEN', '5a13cd99aaa7a4aeafe26ad6296519758b8e32a0')

s = requests.Session()
s.headers['Authorization'] = 'Token {}'.format(PATROWL_AUTH_TOKEN)

def get_assets():
    r = s.get(PATROWL_ENDPOINT+"/assets/api/v1/list")
    print r.text


get_assets()
