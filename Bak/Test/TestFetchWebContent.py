from urllib.parse import quote
from urllib.request import urlopen, Request
import uuid
from bs4 import BeautifulSoup

tryTimes = 1

def fetchWebContent(key: str) -> str:
    target = "2cn.cn"
    search_text = str(key) + "字的字谜"
    global tryTimes
    tryTimes += 1
    sc_content = str(tryTimes) + "-1"
    temp_uuid = str(uuid.uuid1())

    url = "https://www.bing.com/search?q=" + quote(search_text) + "&qs=n&form=QBRE&sp=-1&lq=0&pq=" + quote(search_text) + "&sc=" + sc_content + "&sk=&cvid=" + temp_uuid
    print("url:", url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",  # 模拟浏览器请求
        "Content-Type": "application/json",  # 指定内容类型
        "Authorization": "Bearer your_access_token",  # 添加认证信息
    }
    req = Request(url=url, headers=headers)
    response = urlopen(req).read()

    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        # print(href)
        if href is not None and target in href:
            return href

    return ""


if __name__ == '__main__':
    cn_web_url = fetchWebContent("不")

    print("cn_web_url is {}.".format(cn_web_url))
