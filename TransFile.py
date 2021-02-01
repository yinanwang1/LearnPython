import time

outString = ""

print("START")

with open('/Users/arthurwang/Desktop/time.txt', 'r') as f:
    for line in f.readlines():
        arr = line.split(',')
        print('line is ' + str(line))
        if len(arr) >= 3:
            outString += arr[0]
            outString += ','
            outString += arr[1]
            outString += ','
            time_local = time.localtime(int(arr[2]))
            outString += time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            outString += '\n'


with open('/Users/arthurwang/Desktop/time_out.txt', 'w') as w:
    w.write(outString)

print("END")


