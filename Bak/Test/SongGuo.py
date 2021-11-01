import urllib3
import json
import urllib3.contrib.pyopenssl
import certifi
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

data = {'type': 1, 'location': {'longitude': 115.55544099999997, 'latitude': 28.850794026413279}, 'start_app': 0}
encode_data = json.dumps(data)

print(encode_data)

headers = {
    'Content-Type': 'application/json',
    'clientInfo': r'''{"clientType":"ios","dt":"2019-02-20 16:08:11","parkingMode":2,"idfa":"B54A6FFA-30A4-4B29-8346-02CF0BCA8FB6","channel":"AppStore","net":"none","tz":28800,"screen":"414x736","appVer":"4.6.0","os":"iOS12.1.4","carCityId":"179","cityid":"179","appnm":"ttpinecone","did":"82D2ACD6-BEA9-4C1A-B3C1-3F9C3FA436FE","loc":"30.281414,120.002692,65","model":"iPhone 8 Plus"}''',
    'User-Agent': 'TTPinecone/4.7.0 (iPhone; iOS 12.1.4; Scale/3.00)',
    'App-Signature': r'''WI5wt78wdOLfVzTtnq_Pos8bxciYsN-7i4liDfJ_e8Ku9LjVPKLwLMP-cFdnMEJD_JV-wEQvB_wCkbXMWh2GQUYOaLmIt3mA9NIga5Jmmxcsg27xKQtdV8KZ0nrumKQBgBTW-Wxk69ByV99_WMDMsZ9uuKW4dw3IXhyAnbE4yRk.{"jti":"19D10616","rbd":"81dd71ac","iss":"ttpinecone-ios-4.6.0","ttu":"","uri":"\/app\/v1\/ebike\/nearby_bikes","iat":"1550650091"}''',
}

http = urllib3.PoolManager()
r = http.request('POST',
                     'https://api.songguo7.com/app/v1/ebike/nearby_bikes',
                     body=encode_data,
                     headers=headers
                 )

print(r.data.decode('unicode_escape'))

