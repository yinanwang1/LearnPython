
content = r"""
<item>
        <shape android:shape="rectangle">
            <padding
                android:bottom="1dp"
                android:left="1dp"
                android:right="1dp"
                android:top="1dp" />
            <solid android:color="#"""
content2 = r"""2884f6" />
            <corners android:radius="25dp" />
        </shape>
    </item>"""

number = 20
result = ""

for i in range(number):
    seg = format(int(i * 100 / number), "x")
    value = seg.rjust(2, '0')
    result += content + value + content2

print(result)