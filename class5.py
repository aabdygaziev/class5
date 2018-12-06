import random
import time
score = 0
level = 4
fail = 0
while True:
    a = ''
    for i in range(0, level):
        a += str(random.randint(0, 9))
    print(a)
    time.sleep(2)
    print('\n' * 100)
    b = input()
    if b == a:
        score += 1
        print('your score')
        print(score)
    elif b != a:
        score -= 1
        fail += 1
        print('your score')
        print(score)
        print('# of wrong guesses')
        print(fail)
    if score % level == 0:
        level += 1
    elif score % level !=0:
        level = 4




