# 查找调度任务

uid = "1645188534551346"
type = 7
date = "2022-04-24 18:51:42"

def main():
    import time
    inputDate = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(inputDate))
    content = "http://erp.qeebike.com/#/cityOperation/bikeOperation/data" \
              "/dispatch_salvage_statistics/detail/{}?".format(uid)
    if 7 == type:
        content = "https://erp.qeebike.com/#/cityOperation/bikeOperation/data/dispatch_bike_deploy_history?"
    oneDay = 24 * 60 * 60
    params = {
        'type': type,
        'begin_time': timeStamp - oneDay,
        'end_time': timeStamp + oneDay,
        'name': '美好未来'
    }

    if 7 == type:
        params["uid"] = uid
    from urllib.parse import urlencode
    print(content + urlencode(params, encoding='utf8'))


def test():
    # 时间戳 <==> 时间数组 <==>时间字符串
    # 时间戳 <==> 时间数组 <==>时间字符串获得时间戳
    import time
    time_now = int(time.time())
    print("time_now is {}".format(time_now))
    # 时间戳 => 时间数组
    time_array = time.localtime(time_now)
    print("time_array is {}".format(time_array))
    # 时间数组=>时间戳
    timestamp = time.mktime(time_array)
    print("timestamp is {}".format(timestamp))
    # 时间数组=>时间字符串
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    print("dt is {}".format(dt))
    # 时间字符串=>时间数组
    time_array = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    print("time_array is {}".format(time_array))


if __name__ == '__main__':
    main()
