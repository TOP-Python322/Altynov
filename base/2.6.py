x1 = ord(input())
y1 = int(input())
x2 = ord(input())
y2 = int(input())

if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
    print ('ДА')
else:
    print ('НЕТ')