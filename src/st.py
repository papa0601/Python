from os import system
from random import choice

WHO = ['파파가', '바쭈가', '연두가']
WHEN =['아침에 일어나자 마자', '자기 직전에', '새벽에', '집에 아무도 없을 때', '정오에', '오후에']
WHERE =['방에서', '교실에서', '공원에서', '마트에서', '화장실에서', '컴퓨터 앞에서', '부엌에서', '방에서', '엘리베이터에서', '술집에서', 'PC방에서', '옥상에서', '자유의 여신상 위에서', '에펠탑 위에서', '고래 뱃속에서', '변기속에서']
WHAT = ['공부를', '물 마시기를', '밥 먹기를', '아이쇼핑을', '볼일을', '수면을', '요리를', '인터넷 검색을', '유튜브 시청을', '애니 시청을', '실시간 수업을', '게임을', '코딩을', '3단 발차기를', '앞구르기 3번을', '앞돌기 옆돌기 뒤돌기 3종 세트를', '술 먹방을']
HOW =['물구나무를 서서', '엎드려서', '기어다니며', '팬티만 입고', '샷건을 갈기며', '"앙 기모띠" 라고 외치며', '스카이콩콩을 타고', '선풍기 바람을 쐬며', '강남스타일을 추며', '술을 마시며', '운동을 하며', '컴퓨터를 응시하며']
WHY = ['자랑하고 싶어서', '잘 보이고 싶어서', '관심이 필요해서', '목이 말라서', '배가 고파서', '오줌이 마려워서', '화가 나서', '기분이 좋아서', '게임하고 싶어서', '돈이 부족해서', '고백하고 싶어서', 'X이 마려워서', '인생이 거지 같아서']

while True:
    who = choice(WHO)
    when = choice(WHEN)
    where = choice(WHERE)
    what = choice(WHAT)
    how = choice(HOW)
    why = choice(WHY)

    print('=====================================================================================================')
    print('=<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<육하원칙 생성기>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>=')
    print('= ' + str(who) + ' ' + str(why) + ' ' + str(when) + ' ' +  str(where) + ' ' + str(what) + ' ' + str(how) + '했다.')
    print('= 문장을 다시 생성하려면 Enter를, 종료하려면 0을 입력해주세요.')
    print('=====================================================================================================')
    re = input('>>>')

    if re == '0':
        break
    else:
        system('cls')