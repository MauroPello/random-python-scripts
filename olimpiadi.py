import math
import numpy

print("inizio")
count = 0

'''1
for i in range(100000, 1000000):
    if i % 6 == 0:
        tmp = i
        rev = 0
        while tmp > 0:
            dig = tmp % 10
            rev = rev * 10 + dig
            tmp = tmp // 10
        if i == rev:
            count += 1
'''

'''3 
print(sum(int(digit) for digit in str(20**21+(10**2021+21)**2)))
'''

'''4
all = list()
for a in range(1, 2021 + 1):
    for b in range(1, 2021 + 1):
        tmp = (2 * (a ** 1 / 2)) + (b ** 1 / 2)
        if 2021 >= tmp >= 1 and tmp.is_integer():
            if tmp in all:
                pass
            else:
                all.append(tmp)
                count += 1
'''

'''5
for a in range(0, 14):
    for b in range(0, 14):
        for c in range(0, 14):
            first = 8 ** a + 8 ** b + 8 ** c
            second = 2 ** a + 2 ** b + 2 ** c
            if first % second != 0:
                continue
            count += 1
'''

'''13
for i in range(1, 32):
    reverse_i = int(str(i)[::-1])
    reverse_power_i = int(str(i**2)[::-1])
    if reverse_power_i == reverse_i**2:
        print(f"{i} {i**2} {reverse_power_i} {reverse_i}")
        count += 1
for i in range(1, 32):
    reverse_i = int(str(i).zfill(2)[::-1])
    if reverse_i <= 31:
        print(f"{i:02d} {reverse_i:02d}")
        count += 1
'''

'''16
last = numpy.float128(-13/62)
for i in range(1000):
    print(f"{i}: {last}")
    if last == 0:
        break
    last = (1 - 1/last) % 1
'''

print(count)
print("fine")
