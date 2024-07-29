# -*- coding:utf8 -*-
import json
import math

import openpyxl


# 将数据库中将json字符串保存的经纬度，转化为高德地图可以查看的经纬度格式

# filePath 是输入的文件，按行存放经纬度json字符串
filePath = '/Users/arthurwang/Desktop/1'
end_longitude = 105.3098116
end_latitude = 27.3013018


def convert(resultList):
    coordinateList = []

    for result in resultList:
        coordinateResultList = []
        for coordinate in result:
           oneCoordinate = '[{},{}]'.format(coordinate["longitude"], coordinate["latitude"])
           print("oneCoordinate is ", oneCoordinate)

           coordinateResultList.append(oneCoordinate)

        coordinateResultStr = ','.join(coordinateResultList)

        coordinateList.append(coordinateResultStr)

    return coordinateList

def calculateDistance(longitude, latitude):
    global end_longitude, end_latitude
    try:
        α1 = math.radians(end_longitude)
        β1 = math.radians(end_latitude)
        α2 = math.radians(longitude)
        β2 = math.radians(latitude)

        R = 6378137.0

        result = R * math.acos(math.sin(β1) * math.sin(β2) + math.cos(β1) * math.cos(β2) * math.cos(α2 - α1))
        print(result)
    except Exception as e:
        print(e)


def main():
    file = open(filePath)
    content = file.readline()
    print("开始")
    while content:
        result = json.loads(content)
        for location in result:
            calculateDistance(location["longitude"], location["latitude"])

        content = file.readline()


    file.close()

    print("结束")


if __name__ == '__main__':
    main()
