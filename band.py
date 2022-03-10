from datetime import datetime
import requests
import json
import re

band_path = '/key/band_key.json'

def band_upload(res):

    day = ['월','화','수','목','금','토','일']
    
    with open(band_path, "r") as json_file:
        json_data = json.dump(json_file)

    band_request_url = 'https://openapi.band.us/v2.2/band/post/create'
    band_token = json_data['band_token']
    band_key = json_data['band_key']
    band_contents = ''

    try:
        lunch_data = res.json()["mealServiceDietInfo"][1]['row'][0]["DDISH_NM"]
        lunch_kcal = res.json()["mealServiceDietInfo"][1]['row'][0]["CAL_INFO"]
        lunch_menus = lunch_data.split('<br/>')

        day_num = int(f'{datetime.now().strftime("%w")}')-1
        band_contents += f'{datetime.now().strftime("<b>[%m월 %d일")} {day[day_num]}요일 중식</b>]\n\n'

        for lunch_menu in lunch_menus:
            band_contents += f'{re.sub(r"[0-9.]", "", lunch_menu)}\n'

        band_contents += f'\n총 열량: {lunch_kcal}'

        # 밴드 급식 게시물 업로드
        requests.post(band_request_url, data={'access_token':band_token, 'band_key':band_key, 'content':band_contents,'do_push':True})

        return {'upload_status': '업로드 성공'}
    except:
        return {'upload_status': '업로드 실패'}