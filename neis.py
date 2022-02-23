import requests
from datetime import datetime

def neis():
    neis_request_url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    neis_params = {'KEY':'efe286d0d8b74405934d74218b333f89', 'Type':'json', 'pIndex':1, 'pSize':5, 'ATPT_OFCDC_SC_CODE':'B10', 'SD_SCHUL_CODE':'7010537','MLSV_YMD':f'{datetime.now().strftime("%Y%m%d")}'}
    
    return requests.get(neis_request_url, params=neis_params)