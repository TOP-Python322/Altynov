a = int(input())
if a%400 == 0:
    print('да')
elif a%100 == 0:
    print('нет')
elif a%4 == 0:
    print('да')
else:
    print('нет')