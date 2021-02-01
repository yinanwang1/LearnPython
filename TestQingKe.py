import ssl
import urllib3
import json

param = {
    "pinLng": 119.9997474253178,
    "cityId": 5,
    "pinLat": 30.27550449378062
}

content = 'https://kop.qingqikeji.com/gateway?api=bh.l.nearbyVehicles&sign=0f24a260ae6ea86c9e45df83eaba4e0f&apiVersion=1.0.0&hwId=58955ad8c6b0d54d5643b9540d078309&klnt=119.994596625434&mobileType=iPhone10%2C2&timestamp=1557136372926&userRole=1&osVersion=12.2&osType=1&userId=281474980226989&token=rKVpeBd__1lAuOUAZtasbtsxagUmpW7AGwPT8dlRE8xUyTGuwjAMgOGrPP2zh9hqUtvr27lDgUKRoJWImKrenZn525lIEM6kuQ7jEF7MWngIV1KFmdz_6K9OarWxVatRhb593peZtFKKHcLtl-8k6tFcqzcLhIXkf5nWdX6eNoQHqUWPbwAAAP__&klat=30.27816107855903&appKey=3c87d752eb39498383de33f065b218eb&appVersion=1.8.2&ttid=bh_app'

ssl._create_default_https_context = ssl._create_unverified_context
http = urllib3.PoolManager()
r = http.request('POST',
                 content,
                 body=json.dumps(param).encode('utf-8'),
                 headers={'content-type': 'application/json',
                          'Cookie': 'JSESSIONID=B5316AD162D467841D216C5B0EC118AA',
                          'didi-header-rid': '0a0042fd3ba2e45b71d1b60e101a0303',
                          'wsgsig': 'dd04-h2iyA5n7BB9luAIJx89CItp/5Vsm+PhU4QlZnne/+T8w0L5wMF2axpzj6nKxCD7CtrEtN+547HK34DGR6ELpTc25K4koafJo5/rnTCHxK3qYd0iTwUPiTtrDLuwQcCyl7dZYpDa5IPRM4EOoKhAgT80yqd7ljs01kqmqU+5YAJRPEtWBy/xiQAFB7uRV8jIY4a5v+8/w7nnxDmlYzB1UMA253Hvu0UaVDbaGM+SL6gnWEjZwyqMDh9Ec5OA01Dawyia0j9k/7RRPFfQByAPkM8k781EmEffO4a5v++Hw6ntwFmlYz9xjNbO',
                          'kopds':'%7B%22mbBreaked%22%3A%220%22%2C%22appInSim%22%3A%22false%22%2C%22mobileMac%22%3A%2202%3A00%3A00%3A00%3A00%3A00%22%2C%22utdId%22%3A%22BC64CAC3-9844-415C-A4C0-3764A3D7C575%22%7D'})

print(r.data.decode('utf-8'))


# 经度相差0.03，差不多是2879米
# 纬度相差0.03  差不多是3333米