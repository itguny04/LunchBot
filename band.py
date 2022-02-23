from datetime import datetime
import requests
import re


def band_upload(res):

    day = ['월','화','수','목','금','토','일']
    
    band_request_url = 'https://openapi.band.us/v2.2/band/post/create'
    band_token = 'ZQAAATU1n7jDKuaoXbauBvSQ9jJNOSII54p_R1K-YEkUZNNvkQOK67dTcj1U8vNh57G8zQHYpUbjGj3GRTdQspCW0xy2Fp65dWLqzUxxZqDWveXF'
    band_key = 'AADsgOG4-gZmTHGY0cRQ5764'
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

        return {'STATUS_CODE': 200}
    except:
        return {'STATUS_CODE': 500}