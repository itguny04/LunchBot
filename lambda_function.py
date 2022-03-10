import neis, band

def lambda_handler(event, context):
    res = neis.neis()
    band_result = band.band_uploads(res)
    
    return {'band':band_result['upload_status']}