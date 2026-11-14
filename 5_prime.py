num = int(input('请输入一个大于1的整数：'))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是质数。')
else:
    print(f'{num}不是质数。')
print('100以内的全部数字有：', end='')
for n in range(2, 101):
    is_n_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_n_prime = False
            break
    if is_n_prime:
        print(n, end='')

