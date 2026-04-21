
import requests

r = requests.get(url='http://www.itwhy.org')
print(r.status_code)

r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})
print(r.url)
print(r.text)