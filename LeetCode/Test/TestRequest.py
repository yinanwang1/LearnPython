import requests
import json
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://mobileapi-qa.dbike.co/pay/wxpay/payscore/inner/app/cancel'
data = {'uid': 111, 'payScoreOrderId': "920335246995296256", 'reason': "取消", "token": "1bf9e87c0fc2441d90232d8114195244"}

r = requests.post(url=url, data=json.dumps(data), verify=False)

print(r.request.path_url)
print(r.request.headers)
print(r.request.body)

print(r.headers)
print(r.json())