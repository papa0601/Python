import urllib.request
from time import sleep
import subprocess
from os import system


def clean():
    system('cls')

if True:  # 선택한 버킷과 선택한 버전이 매칭되는지 확인
    Lbukkit = ['Vanilla', 'CraftBukkit', 'Spigot', 'Paper']
    Lbukkitaddmsg = ['[경고] 바닐라는 플러그인을 지원하지 않습니다. 그래도 ', '미완성입니다.', '미완성입니다.', '미완성입니다.']
    Lversionavail = ['1.5.2', '1.7.10', '1.8.9', '1.10.2', '1.12.2', '1.16.5', '1.17.1', '1.18.1']
    Lvanillalinks = ['', '', '', '', '', '', '', '3GyAOJT']

nofly = ''
if True:  # 출력할 메세지를 미리 정의
    Mbukkitexplanation = '[경고] 완성되지 않은 프로그램'  # TODO
    Mbukkitselectionerror ='[오류] 각 버킷에 해당하는 선택지의 번호를 입력해주세요.\n'
    Mbukkitversionselection = '서버의 버전을 입력해주세요. 예)1.18.1\n지원되는 버전 리스트를 보려면 공백을 입력\n\n>>>'
    Mbukkitavaillist = ''  # TODO


while True:  # 원하는 버킷의 종류를 선택
    clean()
    answer = input('[서버를 열 마인크래프트 버킷의 종류를 선택해주세요]\n'
                        '>>>'+nofly+'\n'  # Line 34
                        '1.Vanilla\n'
                        '2.CraftBukkit\n'
                        '3.Spigot\n'
                        '4.Paper\n>>>')
    if answer == '1':  # Vanilla
        clean()
        check = input('Vanilla는 플러그인을 지원하지 않습니다. 그래도 Vanilla를 선택하시겠습니까?(y/n)\n>>>')
        if check == 'y':
            BukkitName = 'Vanilla'
            break
    elif answer == '2':  # CraftBukkit
        clean()
        check = input('CraftBukkit은 아직 미지원')
        if check == 'y':
            BukkitName = 'CraftBukkit'
            break
    elif answer == '3':  # Spigot
        clean()
        check = input('Spigot은 아직 미지원')
        if check == 'y':
            BukkitName = 'Spigot'
            break
    elif answer == '4':  # Paper
        clean()
        check = input('Paper는 아직 미지원')
        if check == 'y':
            BukkitName = 'Paper'
            break
    elif answer == '0':  # 각 버킷에 대한 설명을 제공
        clean()
        input(Mbukkitexplanation)
        clean()
    else:  # Wrong Input
        nofly = '선택지를 올바르게 입력해주세요!'
clean()
strver =''
for i in range(len(Lversionavail)):
    strver += (Lversionavail[i]+' / ')

while True:  # 원하는 서버 버전을 선택 TODO
    ServerVersion = input('[서버의 버전을 입력해주세요]\n'
                          '지원하는 버전: '+strver+'\n\n>>>')
    if ServerVersion in Lversionavail:
        break
    clean()

clean()


InstallationDirectory = ('C:/Minecraft_Server_' + ServerVersion)
system('mkdir ' + InstallationDirectory)
clean()
input('버킷 파일을 다운로드 하겠습니다. 서버가 '+InstallationDirectory+'에 설치될 것 입니다(서버가 설치된 폴더는 설치가 끝난 후 이동할 수 있습니다. \n계속하려면 Enter를 하세요...')
print('버킷 파일을 다운로드하는 중 입니다. 다운로드 경로는 '+InstallationDirectory+'입니다.\n이 단계는 사용자의 인터넷 환경에 따라서 최대 몇 분정도 소요될 수 있습니다.')
Location = Lversionavail.index(ServerVersion)
if BukkitName == 'Vanilla':
    url = ('https://bit.ly/'+Lvanillalinks[Location])

urllib.request.urlretrieve(url, InstallationDirectory + '/Server.jar')
clean()
print('[파일 다운로드가 완료되었습니다. 서버 설치를 시작합니다]')
sleep(1)
with open(InstallationDirectory + '/installer.bat', 'w') as installer:
    installer.write('c:\n')
    installer.write('cd '+InstallationDirectory+'\n')
    installer.write('./start.bat')

with open(InstallationDirectory +'/start.bat', 'w') as starter:
    starter.write('@echo off\n')
    starter.write('java -Xms512M -Xmx1024M -jar Server.jar')

system(InstallationDirectory + '/installer.bat')
clean()
input('[서버 설치가 완료되었습니다]\n[Enter를 눌러 다음단계로 진행함으로써 Mojang Studios의 EULA에 동의하게 됩니다]\n>https://account.mojang.com/documents/minecraft_eula')
neweula = ''
eula = open("C:/Minecraft_Server_1.18.1/eula.txt", 'r')
eulacopy = eula.readlines()
eula.close()
eulacopy[eulacopy.index('eula=false\n')] = 'eula=true'
for i in range(len(eulacopy)):
    neweula += eulacopy[i]
eula = open("C:/Minecraft_Server_1.18.1/eula.txt", 'w')
eula.write(neweula)
eula.close()
properties = open("C:/Minecraft_Server_1.18.1/server.properties", 'r')
propertiescopy = properties.readlines()
properties.close()

 #  수정할 설정의 위치 찾기
locagm = propertiescopy.index('gamemode=survival')
locadif = propertiescopy.index('difficulty=easy')
locaonmd = propertiescopy.index('online-mode=true')
locapvp = propertiescopy.index('pvp=true')
locaport = propertiescopy.index('server-port=25565')
locacmd = propertiescopy.index('enable-command-block=false')
locamxplr = propertiescopy.index('max-players=20')
locawtype = propertiescopy.index('level-type=default')

 #  리스트 0번: 기본값 영어로 1번 기본값 한국어 및 설명 2번 변경값 영어로 3번 변경값 한국어 및 설명
gm = ['survival','서바이벌 모드', 'survival','서바이벌 모드']
dif = ['easy', '쉬움', 'easy', '쉬움']
onmd = ['true', '허용 안 함', 'true', '허용 안 함']
pvp = ['true', '허용', 'true', '허용']
port = ['25565','', '25565','']
cmd = ['false', '허용 안 함', 'false', '허용 안 함']
mxplr = ['20', '최대 20명까지 동시 접속 가능', '20', '최대 20명까지 동시 접속 가능']
wtype = ['default', '일반맵', 'default', '일반맵']




answer = input('[이제부터 서버의 설정을 수정하겠습니다] \n수정을 하지 않고 기본값으로 계속하시려면 q를 입력하시고, 수정 메뉴로 계속하시려면 공백을 입력해주세요.\n>>>')
while True:
    if answer == 'q':
        break
    else:
        while True:
            print('[설정 변경 페이지]===============================================================================')
            print('[1. 서버의 기본 게임 모드를 변경하시겠습니까?] 기본값: {gm[0]} - {gm[1] 현재 설정값: {gm[2]} - {gm[3]}')
            answer = input('1. survival - 서바이벌 모드(기본값)\n'
                           '2. creative - 크리에이티브 모드\n'
                           '3. adventure - 모험 모드\n\n'
                           '변경하려는 설정의 알맞은 번호를 입력하세요 [공백으로 둘 시 기본값 유지]\n'
                           '>>>')
            if answer == '1':
                break

            elif answer == '2':
                gm[2] = 'creative'
                gm[3] = '크리에이티브 모드'
                break

            elif answer == '3':
                gm[2] = 'adventure'
                gm[3] = '모험 모드'
                break

            elif answer == '':
                break

            else:
                clean()
                print('!다시 입력해주세요!')

        while True:
            print('[설정 변경 페이지]===============================================================================')
            print('[2. 서버의 기본 난이도를 변경하시겠습니까?] 기본값: {dif[0]} - dif[1] 현재 설정값: {dif[2]} - {dif[3]}')
            answer = input('1. peaceful - 평화로움\n'
                           '2. easy - 쉬움(기본값)\n'
                           '3. normal - 보통\n'
                           '4. hard - 어려움'
                           '변경하려는 설정의 알맞은 번호를 입력하세요 [공백으로 둘 시 기본값 유지]\n'
                           '>>>')
            if answer == '1':
                dif[2] = 'peaceful'
                dif[3] = '평화로움'
                break

            elif answer == '2':
                break

            elif answer == '3':
                dif[2] = 'normal'
                dif[3] = '보통'
                break

            elif answer == '4':
                dif[2] = 'hard'
                dif[3] = '어려움'
                break

            else:
                clean()
                print('!다시 입력해주세요!')
                
        while True:
            print('[설정 변경 페이지]===============================================================================')
            print('[2. 복돌 유저의 접속을 허용하시겠습니까?] 기본값: {dif[0]} - dif[1] 현재 설정값: {dif[2]} - {dif[3]}')
            answer = input('1. true - 허용 안 함(기본값)\n'
                           '2. false - 허용\n'
                           '변경하려는 설정의 알맞은 번호를 입력하세요 [공백으로 둘 시 기본값 유지]\n'
                           '>>>')
            if answer == '1':
                break
            
            elif answer == '2':
                onmd[2] = 'false'
                onmd[3] = '허용'

            else:
                clean()
                print('!다시 입력해주세요!')

        while True:
            print('[설정 변경 페이지]===============================================================================')
            print('[3. PVP를 허용하시겠습니까?] 기본값: {pvp[0]} - pvp[1] 현재 설정값: {pvp[2]} - {pvp[3]}')
            answer = input('1. true - 허용(기본값)\n'
                           '2. false - 허용 안 함\n'
                           '변경하려는 설정의 알맞은 번호를 입력하세요 [공백으로 둘 시 기본값 유지]\n'
                           '>>>')
            if answer == '1':
                break
            elif answer == '2':
                pvp[2] = 'false'
                pvp[3] = '허용 안 함'

            else:
                clean()
                print('!다시 입력해주세요!')

        while True:





'''
url = 'https://papermc.io/api/v2/projects/paper/versions/'+version+'/builds/'+str(build)+'/downloads/paper-'+version+'-'+str(build)+'.jar'
system('mkdir '+directory+'\AutoBukkitInstallerTemp')
urllib.request.urlretrieve(url, directory+'\AutoBukkitInstaller\Paper_'+version)
'''
