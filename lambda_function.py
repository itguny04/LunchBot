import neis, band, s3

def lambda_handler(event, context):
    res = neis.neis()
    s3_result = s3.s3_upload(res)
    band_result = band.band_uploads(res)
    
    return {'band':band_result['STATUS_CODE'], 's3':s3_result['STATUS_CODE']}

if __name__ == '__main__':
    lambda_handler(1,1)