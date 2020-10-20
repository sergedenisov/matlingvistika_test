txt = open("input.txt", "r")
num = list(txt)

sum = 0
for i in range(0, len(num)):
    sum = sum + int(num[i])

l = len(num)
s =sum
try:
    sum = s /l
except ZeroDivisionError:
    print('0')
else:
    print(s /l)
txt.close()
