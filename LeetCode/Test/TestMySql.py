
import pymysql


try:
    conn = pymysql.connect(host='192.168.30.173', user='bike', passwd='QEj5edLxZDFlFZOh', db='bike_qa', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from u_user')
    data = cur.fetchall()

    for d in data:
        print("nickname: %r" % d[0])

    cur.close()
    conn.close()

except Exception:
    print("发生异常")
