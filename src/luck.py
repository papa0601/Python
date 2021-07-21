from random import randint
while True:
    try:
        while True:
            max = int(input('랜덤으로 지정할 수의 최댓값을 입력해주세요.10~(수가 클수록 확률이 낮아집니다)>>>>'))
            if max > 9:
                break
            print('\n\n\n\n\n')
            print('10이상의 수를 입력해주세요.')
        break
    except:
        print('\n\n\n\n\n')
        print('정수를 입력해주세요.')
goal = randint(0, max) + 10
cur = 1
att = 0
while (cur != goal):
    cur = randint(0, goal) + 1
    att = att + 1
    print(str(att) + '번째 시도 : 실패');
att = att + 1
print(str(att) + '번째 시도 : 성공!')