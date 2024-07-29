# -*- coding:utf8 -*-
import json
import openpyxl


# baofu分账金额查询

# filePath 分账的数据
filePath = '/Users/arthurwang/Desktop/test1'

# fileSavePath 输出为转换好的文件
fileSavePath = '/Users/arthurwang/Desktop/output.xlsx'


def save(resultList):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "分账金额"

    row = 1
    for money in resultList:
        print("money is ", money)
        sheet.cell(row, 1, money).number_format = '0'

        row += 1

    wb.save(fileSavePath)


def main():
    file = open(filePath)
    content = file.readline()
    resultList = []
    while content:
        print('content is ', content)
        result = content.split('|')
        if "CM660000000109681238" == result[20]:
            resultList.append(result[21])

        content = file.readline()

    print('resultList is ', resultList)

    save(resultList)

    file.close()


if __name__ == '__main__':
    main()
