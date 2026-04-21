import json
from time import sleep
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup


# 获取网页的的字谜，此时的操作是获取到所有的字谜
# 保存到桌面的other.json中
# 避免请求太过平凡，中间加一个1秒的延迟

global_session = None

def create_session_with_retry(max_retries=3):
    # 配置重试策略
    retry_strategy = Retry(
        total=max_retries,  # 最大重试次数
        backoff_factor=1,  # 重试间隔时间因子（秒），计算公式：{backoff_factor} * (2 **({retry_number} - 1))
        status_forcelist=[429, 500, 502, 503, 504],  # 需要重试的状态码
        allowed_methods=["GET"]  # 只对GET请求重试（默认包含所有方法，可根据需求调整）
    )

    # 创建适配器并挂载到session
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session

def fetchWebContent(key: str) -> list:
    """
    根据索引号获取当前页面的所有字谜的链接
    :param key:
    :return:
    """
    index = "index"
    if key != "1":
        index = index + "_" + str(key)
    url = "https://2cn.cn/fl/xiaoxueshengzimi/" + str(index) + ".html"
    # print("url:", url)
    # 创建一个最大重试3次的session
    try:
        response = global_session.get(url)
    except Exception as e:
        print(e)
        return []
    if 200 != response.status_code:
        print("请求失败，错误码为" + str(response.status_code))
        return []
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    resultList = []
    for link in links:
        href = link.get('href')
        # print(href)
        if href is not None and href.startswith('/my'):
            resultList.append(href)

    return resultList


def fetchPuzzle(link: str) -> dict:
    """
    获取字谜的内容
    :param link:
    :return:
    """
    url = "https://2cn.cn" + link
    print("url:", url)
    try:
        response = global_session.get(url)
    except Exception as e:
        print(e)
        return {}
    if 200 != response.status_code:
        print("url " + url + "请求失败")
        return {}
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='text_info')
    # print("content is {}".format(str(content)))
    if content is None:
        return {}
    div_content = content.find_all("div")
    # print("div_content is {}".format(str(div_content)))
    if div_content is None:
        return {}
    result = {}
    question = {}
    question_text = "谜面"
    answer_text = "谜底"
    tips_text = "提示"
    for div in div_content:
        # print("div is {}".format(str(div)))
        h2 = div.find('h2', class_='h2')
        p = div.find('p')
        if p is None or h2 is None:
            continue

        h2_text = h2.text
        p_text = p.text
        # print("h2_text is {}".format(str(h2_text)))
        # print("p_text is {}".format(str(p_text)))
        if h2_text == answer_text:
            result["w"] = p_text
        else:
            if h2_text == question_text:
                question["r"] = p_text
            elif h2_text == tips_text:
                question["a"] = p_text
    result["p"] = [question]

    return result


def saveToFile(puzzle: dict):
    """
    将获取到的字谜保存到文件中
    :param puzzle:
    :return:
    """
    with open("/Users/arthurwang/Desktop/other.json", "a+", encoding="utf-8") as f:
        json_str = json.dumps(puzzle, ensure_ascii=False)
        f.write(json_str + ",\n")

def fetchAllPuzzles():
    for i in range(6, 57):
        print("index is {}".format(i))
        cn_web_url = fetchWebContent(str(i))
        # print("cn_web_url is {}.".format(cn_web_url))
        for url in cn_web_url:
            puzzle = fetchPuzzle(url)
            if not puzzle:
                continue
            # print("puzzle is " + str(puzzle))
            # 写入文件
            saveToFile(puzzle)
            # 等待一秒，避免服务器的压力过大
            sleep(1)

retry_urls = [

]

def refetchFailedPuzzles():
    for url in retry_urls:
        puzzle = fetchPuzzle(url)
        if not puzzle:
            continue
        # print("puzzle is " + str(puzzle))
        # 写入文件
        saveToFile(puzzle)
        # 等待一秒，避免服务器的压力过大
        sleep(1)

if __name__ == '__main__':
    global_session = create_session_with_retry(max_retries=3)
    fetchAllPuzzles()
    # refetchFailedPuzzles()

