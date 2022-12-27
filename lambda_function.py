from datetime import datetime
import re, requests, json


def lambda_handler(event, context):
    
    with open('key.json', 'r') as f:
        api_key = json.load(f)
        
    # mealApi(neis)
    mealApi_url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    mealApi_params = {'KEY':api_key['neis']['KEY'], 'Type':'json', 'pIndex':1, 'pSize':5, 'ATPT_OFCDC_SC_CODE':'B10', 'SD_SCHUL_CODE':'7010537','MLSV_YMD':f'{datetime.now().strftime("%Y%m%d")}'}
    
    mealApi_res = requests.get(mealApi_url, params=mealApi_params)
    
    # postLunch(naver band)
    day = ['월','화','수','목','금','토','일']
    
    band_request_url = 'https://openapi.band.us/v2.2/band/post/create'
    band_token = api_key['band']['token']
    band_key = api_key['band']['key']
    band_contents = ''

    meal_raw = mealApi_res.json()["mealServiceDietInfo"][1]['row'][0]["DDISH_NM"].split('<br/>')
    meal_kcal = mealApi_res.json()["mealServiceDietInfo"][1]['row'][0]["CAL_INFO"]
        
    day_num = int(f'{datetime.now().strftime("%w")}')-1
    band_contents += f'{datetime.now().strftime("<b>[%m월 %d일")} {day[day_num]}요일 중식]</b>\n\n'

    for meal in meal_raw:
        band_contents += f'{re.sub(r"[^가-힣]", "", meal)}\n'
        
    band_contents += f'\n총 열량: {meal_kcal}\n\n'
    
    # 밴드 급식 게시물 업로드
    requests.post(band_request_url, data={'access_token':band_token, 'band_key':band_key, 'content':band_contents, 'do_push':True})

    return {'health':200}