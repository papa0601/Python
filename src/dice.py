from random import randint
while True:
    rannum = randint(1,6)
    print('주사위의 수는 ' + str(rannum) + '입니다.\n')
    con = input('나가려면 0을 입력하세요. 1을 입력하면 주사위를 다시 굴리게 됩니다>>>')
    if con == '0':
        break
    i = 0
    for i in range(25):
        print('')