# -*- coding:utf8 -*-
import json
import openpyxl


# 将数据库中将json字符串保存的经纬度，转化为高德地图可以查看的经纬度格式

# filePath 是输入的文件，按行存放经纬度json字符串
filePath = '/Users/arthurwang/Desktop/1'

# fileSavePath 输出为转换好的文件
fileSavePath = '/Users/arthurwang/Desktop/output.xlsx'


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


def save(resultList):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "经纬度"

    value = convert(resultList)
    row = 1
    for coordinateStr in value:
        print("coordinateStr is ", coordinateStr)
        sheet.cell(row, 1, coordinateStr)

        row += 1

    wb.save(fileSavePath)


def main():
    file = open(filePath)
    content = file.readline()
    resultList = []
    while content:
        print('content is ', content)
        result = json.loads(content)
        resultList.append(result)

        content = file.readline()

    print('resultList is ', resultList)

    save(resultList)

    file.close()


if __name__ == '__main__':
    main()
