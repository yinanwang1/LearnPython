# 从桌面的log日志文件中获取单车type为44的内容，保存为json，然后直接用于/dispatcher/query/trajectory/list接口展示

import json

import gps_transfomer

battery_quantity = 'battery_quantity'
location = 'location'
battery_time = 'battery_time'


def fetchType44(content: str) -> dict:
    try:
        item_list = content.split(":")
        message_content = item_list[-1]
        values = message_content.split(",")
        print(values)
        if len(values) != 5:
            return None

        time_temp = values[-1] if values[-1] else "0"
        (g_lng, g_lat) = gps_transfomer.trans_ddmm_to_dd(float(values[2]), float(values[3]))
        (lng, lat) = gps_transfomer.wgs84_to_gcj02(g_lng, g_lat)

        result = dict()
        result["coordinates"] = {
            "longitude": lng,
            "latitude": lat
        }
        result["time"] = time_temp

        return result

    except Exception as e:
        print(e)
        return None


def save(resultList):
    response = {
        "status": 1,
        "msg": "",
        "data": {
            "list": resultList
        }
    }
    with open('/Users/arthurwang/Desktop/time_out.json', 'w') as w:
        w.write(json.dumps(response))


def main():
    names = ['/Users/arthurwang/Desktop/fromNewToOld.json',
             '/Users/arthurwang/Desktop/fromNewToOld2.json']

    # 包含type=4的内容的model
    location_list = list()

    for name in names:
        with open(name, "r") as fo:
            whole_content = fo.read()
            if not whole_content:
                continue
            type44_content = json.loads(whole_content)
            hits = type44_content["responses"][0]["hits"]["hits"]
            print(len(hits))
            for hit in hits:
                message = hit["_source"]["message"]
                if message:
                    result = fetchType44(message)
                    if result:
                        location_list.append(result)

    save(location_list)


if __name__ == "__main__":
    main()
