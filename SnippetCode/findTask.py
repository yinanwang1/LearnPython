# 查找调度任务

uid = "1620065136624958"
type = 0
date = "2017-08-31 19:52:06"


def main():
    import time
    inputDate = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(inputDate))
    content = "http://erp.qeebike.com/#/cityOperation/bikeOperation/data" \
              "/dispatch_salvage_statistics/detail/{}?type={}" \
              "&begin_time={}&end_time={}&name=%u5218%u65ED%u660E"
    oneDay = 24 * 60 * 60
    result = content.format(uid, type, timeStamp - oneDay, timeStamp + oneDay)
    print(result)


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
