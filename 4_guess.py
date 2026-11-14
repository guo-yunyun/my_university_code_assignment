import random

target = random.randint(1, 100)
guess_count = 0
print('欢迎来到猜数字游戏！我已想好了一个1到100内的整数数字，快来猜猜！')
while True:
    guess = int(input('请输入你猜的整数数字：'))
    guess_count += 1
    if guess > target:
        print('大了')
    elif guess < target:
        print('小了')
    else:
        print(f'恭喜你猜中了！数字就是{target}')
        break
