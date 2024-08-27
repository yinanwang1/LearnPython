#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

content = "挪蒸秧萎番锻雅勃旬熬蒜醋饺翡拌榛栗筝鞭麦寺逛籍屉怖瞅魔胖刑哼峻残匪窝啃舅鸿鼎旺炊乖裙兜币哎橱锈摩揉玛蘸毒撇噎搓匣喳吭娜伊搅埃伦藤析碱顽卓效蚀乏誉衔粪捐澡械逆玫域"

def main():
    result = list()
    words = list(content)
    for word in words:
        wordObj = dict()
        wordObj["word"] = word
        wordObj["puzzles"] = list()

        result.append(wordObj)

    print(json.dumps(result))


if __name__ == '__main__':
    main()