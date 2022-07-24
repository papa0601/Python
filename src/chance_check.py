from random import choice
from math import trunc

list = [-1, 1]
attempt = 0
number = 0
numsum = 0
plus = 0
minus = 0
chansum = 0

uptime = 0

def space():
    print('    ', end='')

while True:
    attempt += 1
    rannum = choice(list)

    number += rannum

    if rannum == 1:
        plus += 1

    else:
        minus -= 1


    chance = round((plus / attempt) * 100, 3)

    if chance >= 50:
        status = '+'
    else:
        status = '-'

    numsum += number
    avgnum = trunc(numsum / attempt)

    chansum += chance
    avgchan = round(chansum / attempt, 3)

    numstat = str(trunc(number / 100)*100).replace('-', '')

    if number > 0:
        uptime += 1

    upchan = round((uptime / attempt)*100, 3)



    if chance > 50.01:
        pp = round(number / trunc((chance - 50) * 100), 3)
        m = 0

    elif chance < 49.99:
        pp = round(number / trunc((50 - chance) * 100), 3)*-1
        m = 0

    else:
        m = 1




    print('[Attempt] ', attempt, end='')
    space()
    print('[Current] ', number, end='')
    space()
    print('[Current_AVG] ', avgnum, end='')
    space()
    print('[Current_STAT] ', status, numstat, end='')
    space()
    print('[Added] ', plus, end='')
    space()
    print('[Minus] ', minus, end='')
    space()
    print('[Chance] {:.2f}%'.format(chance), end='')
    space()
    print('[Chance_AVG] {:.2f}%'.format(avgchan), end='')
    space()
    print('[UpTime] {:.2f}%'.format(upchan), end='')
    space()
    if m == 0:
        print('[Exchange] {:.2f} per 0.01%'.format(pp), end='')
    else:
        print('[Exchange] Cannot Be Measured!', end='')

    print('')