import  random
import time
batman = 100
robin = 100
hit = 15
block = 5
kick = 20
while True:
    who = int(random.randint(1, 2))
    if who == 1:
        print('batman hits robin')
        a = ''
        a = int(random.randint(1, 12))
        print('sila udara', a)
        time.sleep(1.5)
        print('\n'*100)
        if a in range (1, 5):
            robin -= hit*0
        elif a in range (6, 7):
            robin -= hit*0.25
        elif a in range (8, 9):
            robin -= hit*0.5
        elif a in range (10, 11):
            robin -= hit * 0.75
        elif a in range(10, 11):
            robin -= hit * 0.75
        elif a == 12:
                robin -= hit * 1
        print('batmans health', batman)
        print ('robins health', robin)
    elif who == 2:
        print('robin hits robin')
        b = ''
        b = int(random.randint(1, 12))
        print('sila udara', b)
        time.sleep(1.5)
        print('\n' * 100)
        if b in range(1, 5):
            batman -= hit * 0
        elif b in range(6, 7):
            batman -= hit * 0.25
        elif b in range(8, 9):
            batman -= hit * 0.5
        elif b in range(10, 11):
            batman -= hit * 0.75
        elif b in range(10, 11):
            batman -= hit * 0.75
        elif b == 12:
            batman -= hit*1
        print('batmans health', batman)
        print('robins health', robin)



