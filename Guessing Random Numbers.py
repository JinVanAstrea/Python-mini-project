import random
print('--------------Guess the number--------------')
answer=random.randint(0,100)
num=0	
while True:
    num= num + 1
    guess=int(input('Enter the number you are guessing(1-100)：'))
    if guess==answer:
        print('you are correct！' )
        print('game over！')
        break
    elif guess>answer:
        print('too big！' )
    elif guess<answer:
        print('too small！' )
print('guess' , num, 'times' )

