import pycurl
from io import BytesIO
import os
import subprocess

curl_content = '''
curl 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH000300&begin=1727674368857&period=day&type=before&count=-284&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'cookie: cookiesu=851727586821390; device_id=ba36611a722e97e9f7cd06248543d92b; xq_a_token=3bcf4426f1cc0d0e14b213b22f45ef825638a2d7; xqat=3bcf4426f1cc0d0e14b213b22f45ef825638a2d7; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjU4NTE1Mzk2NDIsImlzcyI6InVjIiwiZXhwIjoxNzMwMTc4ODYzLCJjdG0iOjE3Mjc1ODY4NjM4NTgsImNpZCI6ImQ5ZDBuNEFadXAifQ.kgsopr-4_t3NwSR8NQU_vXbePq8wihAJjTxmTQr3Vi_0-oqT4DNz-fycJvT6wpWzYkQ6LXtAFVaqVe84IczFOGcMzSsv9vnZx9U_CDHtMzepPDxEJhGsphQc3RXYnEhWfEtmu_U0w5wWxjw-aK1qTIKIMU2aUFoNFhITIzF61Ot087A_kNqD6RqmJzCs1dHvt9jkE1sVHfEoN1yy5ehen1rAYcCsMt5b6RsIGny4JpxpLz8Tk3vhm4eUJb9SMzzR9wqkfluiGtga275lcE0684zOO2bfvpviY2j5zP5AHHymwC6A4uJh5zUO0BPIoPp0KaOsOvnSZ4jy02PoHn5zxQ; xq_r_token=bcc484a11645d236ba12d02746449199c5822d5f; xq_is_login=1; u=5851539642; ssxmod_itna=Qqfx0DgGD=dGqiKGHiGdISeeqBKYv0hu7oChw+kibqGN=4oGRDCqAPGfDIbR/2G+xY5YiAchaqQ702dD9GDbdY183RgWwCCAr43D=xYQDwxYo8DATKD97xeiiDC40rD74irDDxD3XxDvsLoqDjmvC9EyHRGF7Lp5DbaqDmoqDROoDS7YG4IyH8BO7DGHhBiqDugvQwxi8D7KLRYOzD7ppvR3DXrqDEnRCgIdDvcgOwaxsVPAQlb24T6GeDxhqb7mKqAhqQ70DtP=QeBecWhiQ3Dhgd0nKWY6nDDpKKncljYD; ssxmod_itna2=Qqfx0DgGD=dGqiKGHiGdISeeqBKYv0hu7oChw+kDA6chpxYD/nCCDFgmMFe0IBO8nCMu6xKAOGARwRFCkHTp3ojYg=D6Ax4ren0h67TYeRzRYR8IdyWwR0B89ddMON57WwQUqHBau4K0pbziD=yAWqzZeeYmvQ72hwZQWwi9uCt0Kb7aR=8iGwqQDmNloIKOa7Azv4tnwQYl9FuaGQqQeFZCH8XPBwNhaxK=w0O=i6ff2Cho3ELIp7SEP7mOnudva5Axoegfxz=EPuk2=FtfaWPwH7hLHUbMWnrpFnUqgyq=8EOPPj1Ip82o92KjOIWhXw26yYiO00PK=wDLECwsBieZohn=+7UhAey0EhYb4A53/+VgKQ3thAbthqI0EGENah574o9ENmi2fCrpGEz/oxxnqDn7DWDZj17=2cACmudhqalAu6qejolhjNxxUjRzjq0PUx8GRBKr4hs9xIcDUaqKKF8Dx0nqrcLC2xzoqEKEvUdSe5mnwRYjV3qbIPrZtNUmV0jB/A7CQU+m6K=SKLAENZYTUf5UGpL/IL4ijiBNvpBWQnrXUOyt4IyKoat6xh00AR+rFuhwv8k42he8uzkU8z6aDG2lwiTo5CGw+dHbziK4u1zeRYEbgRbeQFb595dcztBUmURFYxrexW94x7N=QMgwMHoii/BR3TCdTGbCKqQSoMFdNY0DfmHxZiLywDvqtGqDGcDD2QDxD===' \
  -H 'dnt: 1' \
  -H 'origin: https://xueqiu.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://xueqiu.com/S/SH000300' \
  -H 'sec-ch-ua: "Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
'''

http_content = r'''
https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH000300&begin=1727674368857&period=day&type=before&count=-284&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance \
  -H accept: application/json, text/plain, */* \
  -H accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7 \
  -H cookie: cookiesu=851727586821390; device_id=ba36611a722e97e9f7cd06248543d92b; xq_a_token=3bcf4426f1cc0d0e14b213b22f45ef825638a2d7; xqat=3bcf4426f1cc0d0e14b213b22f45ef825638a2d7; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjU4NTE1Mzk2NDIsImlzcyI6InVjIiwiZXhwIjoxNzMwMTc4ODYzLCJjdG0iOjE3Mjc1ODY4NjM4NTgsImNpZCI6ImQ5ZDBuNEFadXAifQ.kgsopr-4_t3NwSR8NQU_vXbePq8wihAJjTxmTQr3Vi_0-oqT4DNz-fycJvT6wpWzYkQ6LXtAFVaqVe84IczFOGcMzSsv9vnZx9U_CDHtMzepPDxEJhGsphQc3RXYnEhWfEtmu_U0w5wWxjw-aK1qTIKIMU2aUFoNFhITIzF61Ot087A_kNqD6RqmJzCs1dHvt9jkE1sVHfEoN1yy5ehen1rAYcCsMt5b6RsIGny4JpxpLz8Tk3vhm4eUJb9SMzzR9wqkfluiGtga275lcE0684zOO2bfvpviY2j5zP5AHHymwC6A4uJh5zUO0BPIoPp0KaOsOvnSZ4jy02PoHn5zxQ; xq_r_token=bcc484a11645d236ba12d02746449199c5822d5f; xq_is_login=1; u=5851539642; ssxmod_itna=Qqfx0DgGD=dGqiKGHiGdISeeqBKYv0hu7oChw+kibqGN=4oGRDCqAPGfDIbR/2G+xY5YiAchaqQ702dD9GDbdY183RgWwCCAr43D=xYQDwxYo8DATKD97xeiiDC40rD74irDDxD3XxDvsLoqDjmvC9EyHRGF7Lp5DbaqDmoqDROoDS7YG4IyH8BO7DGHhBiqDugvQwxi8D7KLRYOzD7ppvR3DXrqDEnRCgIdDvcgOwaxsVPAQlb24T6GeDxhqb7mKqAhqQ70DtP=QeBecWhiQ3Dhgd0nKWY6nDDpKKncljYD; ssxmod_itna2=Qqfx0DgGD=dGqiKGHiGdISeeqBKYv0hu7oChw+kDA6chpxYD/nCCDFgmMFe0IBO8nCMu6xKAOGARwRFCkHTp3ojYg=D6Ax4ren0h67TYeRzRYR8IdyWwR0B89ddMON57WwQUqHBau4K0pbziD=yAWqzZeeYmvQ72hwZQWwi9uCt0Kb7aR=8iGwqQDmNloIKOa7Azv4tnwQYl9FuaGQqQeFZCH8XPBwNhaxK=w0O=i6ff2Cho3ELIp7SEP7mOnudva5Axoegfxz=EPuk2=FtfaWPwH7hLHUbMWnrpFnUqgyq=8EOPPj1Ip82o92KjOIWhXw26yYiO00PK=wDLECwsBieZohn=+7UhAey0EhYb4A53/+VgKQ3thAbthqI0EGENah574o9ENmi2fCrpGEz/oxxnqDn7DWDZj17=2cACmudhqalAu6qejolhjNxxUjRzjq0PUx8GRBKr4hs9xIcDUaqKKF8Dx0nqrcLC2xzoqEKEvUdSe5mnwRYjV3qbIPrZtNUmV0jB/A7CQU+m6K=SKLAENZYTUf5UGpL/IL4ijiBNvpBWQnrXUOyt4IyKoat6xh00AR+rFuhwv8k42he8uzkU8z6aDG2lwiTo5CGw+dHbziK4u1zeRYEbgRbeQFb595dcztBUmURFYxrexW94x7N=QMgwMHoii/BR3TCdTGbCKqQSoMFdNY0DfmHxZiLywDvqtGqDGcDD2QDxD=== \
  -H dnt: 1 \
  -H origin: https://xueqiu.com \
  -H priority: u=1, i \
  -H referer: https://xueqiu.com/S/SH000300 \
  -H sec-ch-ua: "Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129" \
  -H sec-ch-ua-mobile: ?0 \
  -H sec-ch-ua-platform: "macOS" \
  -H sec-fetch-dest: empty \
  -H sec-fetch-mode: cors \
  -H sec-fetch-site: same-site \
  -H user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0
'''

result = os.system(curl_content)
print("result is {}".format(result))

# buffer = BytesIO()
# c = pycurl.Curl()
# c.setopt(c.URL, curl_content)
# c.setopt(c.WRITEDATA, buffer)
# c.perform()
# c.close()
#
# body = buffer.getvalue()
# print(body.decode('utf-8'))

# result = subprocess.run(['curl', http_content], capture_output=True, text=True)
# print("result is {}".format(result.stdout))