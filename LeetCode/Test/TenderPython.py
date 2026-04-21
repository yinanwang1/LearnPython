import re

content = '1234567893'
# regex = re.compile()
x = re.match(r"[%&',;=?$]+", content, re.I)
try:
    print(x)
    print(len(x))
    # print(type(x))
    # print(x.group()
    # print(x.span())
except Exception as e:
    print(e)
