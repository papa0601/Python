import urllib.request
from time import sleep
from os import system
from random import randint

def cls():
    system('cls')

 #버킷과 버전 선택 페이지

BukkitType_msg = ''
while True:
    print('Step1. 버킷 종류 및 버전 선택')
    print('[설치할 버킷의 종류를 골라주세요] - ' + BukkitType_msg)
    print('')
    print('1. Vanilla/바닐라')
    print('')
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
    print('[설치할 버킷의 버전을 골라주세요] - ' + BukkitVersion_msg)
    print('')
    print('1. 1.18.1')
    print('')
    BukkitVersion_s = input('>>>')

    if BukkitVersion_s == '1':
        BukkitVersion = '1.18.1'
        break

    else:
        cls()
        BukkitVersion_msg = '(오류) 선택지가 올바르지 않습니다. 선택지의 번호를 올바르게 입력해주세요.'
        pass

 #다운로드 설정 페이지

cls()
print('Step2. 버킷 다운로드')
print('')
print('[이제 해당하는 버전의 버킷을 다운로드 하겠습니다]')
print('[버킷은 C:\에 새 폴더를 만들고 그 폴더 안에 설치됩니다]')
print('[버킷이 설치된 후 폴더의 이름을 바꾸거나 폴더를 이동해도 문제는 발생하지 않습니다]')
print('[버킷을 설치하기 위해서는 최소 150MB의 공간이 필요하며 정상적인 서버 구동을 위해 500MB이상의 여유공간이 필요합니다]')
print('[이 내용을 모두 확인하셨다면 Enter를 입력해주세요]')
print('')
input('>>>')

cls()
EulaAgreement_msg = ''
while True:
    print('Step2. 버킷 다운로드 - ' + EulaAgreement_msg)
    print('')
    print('[마인크래프트 버킷을 설치하고 사용하기 위해서는 Minecraft Eula에 동의해야 합니다.]')
    print('[https://account.mojang.com/documents/minecraft_eula를 방문하여 Eula의 내용을 확인하세요]')
    print('[이를 확인하시고 Eula에 동의하신다면 [y]를 입력해주세요')
    print('')
    EulaAgreement_s = input('>>>')

    if EulaAgreement_s == 'y':
        break

    else:
        cls()
        EulaAgreement_msg = '(오류) Eula에 동의하지 않을경우 설치를 계속할 수 없습니다.'
        pass

cls()
BukkitDownload_msg = ''
FolderName = 'Minecraft_Server-'+str(randint(1, 100))
InstallationDirectory = 'C:/'+FolderName
system('mkdir ' + InstallationDirectory)

try:
    print('Step2. 버킷 다운로드 - ' + BukkitDownload_msg)
    print('')
    print('-설치 위치 지정하기 -> 완료 (' + InstallationDirectory + ')')
    print('-설치 폴더 생성하기 -> 완료')
    print('-버킷파일 다운로드하기 -> 다운로드 중...')
    print('-버킷 설치하기 -> 대기 중...')
    print('-버킷 설정하기 -> 대기 중...')


except:
    pass

 #버킷 설치 페이지





 #설치 후 설정 페이지