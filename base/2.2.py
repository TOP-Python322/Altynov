a = int(input())
b = int(input())
if a % b == 0:
    print(f'{a} делится на {b} нацело')
    print(f'частное: {(a//b)}')
else:
    print(f'{a} не делится на {b} нацело')
    print(f'неполное частное: {(a//b)}')
    print(f'остаток: {(a%b)}')