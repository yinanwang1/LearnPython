import ssl
import urllib3
import json

param = {
         "currentLng": 119.99735470920138,
         "bikeTabType": 1,
         "radius": 2000,
         "version": "5.14.0",
         "cityCode": "0571",
         "action": "user.ride.nearBikes",
         "platform": 2,
         "token": "9c51a74fec0340a79c0378853220b4af",
         "lat": 30.281886337148075,
         "sourceId": "a0029999",
         "lng": 120.01372359462188,
         "appVersion": "5.14.0",
         "systemCode": "61",
         "adCode": "330110",
         "currentLat": 30.275064524739584
}

ssl._create_default_https_context = ssl._create_unverified_context
http = urllib3.PoolManager()
r = http.request('POST',
                 'https://bike.hellobike.com/api',
                 body=json.dumps(param).encode('utf-8'),
                 headers={'content-type': 'application/json'})

print(r.data.decode('utf-8'))

print(json.loads(r.data.decode('utf-8'))["data"])


# 经度相差0.03，差不多是2879米
# 纬度相差0.03  差不多是3333米
