import requests
from datetime import datetime
import json

neis_path = './key/neis_key.json'

def neis():
    with open(neis_path, 'r') as json_file:
        json_data = json.dump(json_file)

    KEY = json_data['KEY']
    ATPT_OFCDC_SC_CODE = json_data['ATPT_OFCDC_SC_CODE']
    SD_SCHUL_CODE = json_data['SD_SCHUL_CODE']

    neis_request_url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    neis_params = {'KEY':KEY, 'Type':'json', 'pIndex':1, 'pSize':5, 'ATPT_OFCDC_SC_CODE':ATPT_OFCDC_SC_CODE, 'SD_SCHUL_CODE':SD_SCHUL_CODE,'MLSV_YMD':f'{datetime.now().strftime("%Y%m%d")}'}
    
    return requests.get(neis_request_url, params=neis_params)