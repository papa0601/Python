import urllib.request
from time import sleep
from os import system

def cls():
    system('cls')

 #버킷과 버전 선택 페이지

BukkitType_msg = ''
while True:
    print('Step1. 버킷 종류 및 버전 선택')
    print('[설치할 버킷의 종류를 골라주세요]')
    print(BukkitType_msg)
    print('1. Vanilla/바닐라')
    print('\n')
    BukkitType_s = input('>>>')

    if BukkitType_s == '1':
        BukkitType = 'Vanilla'
        break

    else:
        cls()
        BukkitType_msg = '(오류) 선택지가 올바르지 않습니다. 선택지의 번호를 올바르게 입력해주세요.'
        pass

cls()
BukkitVersion_msg = ''
while True:
    print('Step1. 버킷 종류 및 버전 선택')
    print('[설치할 버킷의 버전을 골라주세요]')
    print(BukkitVersion_msg)
    print('1. 1.18.1')
    print('\n')
    BukkitVersion_s = input('>>>')

    if BukkitVersion_s == '1':
        BukkitVersion = '1.18.1'
        break

    else:
        cls()
        BukkitVersion_msg = '(오류) 선택지가 올바르지 않습니다. 선택지의 번호를 올바르게 입력해주세요.'
        pass

 #다운로드 설정 페이지





 #버킷 설치 페이지





 #설치 후 설정 페이지