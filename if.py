number = 23
while True:

    guess = int(input('请输入一个整数：'))
    if guess == number:
        print('恭喜，你猜对了。')
        break
    elif guess < number:
        print('你猜小了')
    else:
        print('你猜大了')

print('end') 
