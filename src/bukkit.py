import urllib.request
import urllib.error
from os import system


def clean():
    system('cls')

if True:  # 선택한 버킷과 선택한 버전이 매칭되는지 확인
    Lbukkit = ['Vanilla', 'CraftBukkit', 'Spigot', 'Paper']
    Lbukkitaddmsg = ['[경고] 바닐라는 플러그인을 지원하지 않습니다. 그래도 ', '미완성입니다.', '미완성입니다.', '미완성입니다.']
    Lversionexist = ['1.5.2', '1.7.10', '1.8.9', '1.10.2', '1.12.2', '1.16.5', '1.17.1', '1.18.1']
    Lvanillalinks = ['', '', '', '', '', '', '', '3GyAOJT']


if True:  # 출력할 메세지를 미리 정의
    Mbukkitselection = ('서버를 열 마인크래프트 버킷의 종류를 선택해주세요.\n'  # Line 34
                        '1.Vanilla\n'
                        '2.CraftBukkit\n'
                        '3.Spigot\n'
                        '4.Paper\n\n'
                        '[각 버킷에 대한 설명을 보려면 0을 입력하세요]\n>>>')
    Mbukkitcheck = '을(를) 선택하시겠습니까?'
    Mbukkitexplanation = '[경고] 완성되지 않은 프로그램'  # TODO
    Mbukkitselectionerror ='[오류] 각 버킷에 해당하는 선택지의 번호를 입력해주세요.\n'
    Mbukkitversionselection = '서버의 버전을 입력해주세요. 예)1.18.1\n지원되는 버전 리스트를 보려면 공백을 입력\n\n>>>'
    Mbukkitavaillist = ''  # TODO
    Mserverversiondoesnotexists = '[오류] 해당 버전을 위한 버킷이 없습니다. 지원 리스트를 확인하시고 다시 입력해주세요.'
    Mserverdirectory = '마인크래프트 서버를 설치할 파일 경로를 입력해주세요.\n공백으로 비워둘 경우 자동으로 '+'C:\ '.replace(' ', '')+'아래에 설치됩니다.'

while True:  # 원하는 버킷의 종류를 선택
    answer = input(Mbukkitselection)
    if answer == '1':  # Vanilla
        clean()
        check = input(Lbukkitaddmsg[0]+Lbukkit[0]+'를 선택하시겠습니까?(y/n)\n>>>')
        if check == 'y':
            BukkitName = 'Vanilla'
            break
    elif answer == '2':  # CraftBukkit
        clean()
        check = input(Lbukkitaddmsg[1]+Lbukkit[1])
        if check == 'y':
            BukkitName = 'CraftBukkit'
            break
    elif answer == '3':  # Spigot
        clean()
        check = input(Lbukkitaddmsg[2]+Lbukkit[2])
        if check == 'y':
            BukkitName = 'Spigot'
            break
    elif answer == '4':  # Paper
        clean()
        check = input(Lbukkitaddmsg[3]+Lbukkit[3])
        if check == 'y':
            BukkitName = 'Paper'
            break
    elif answer == '0':  # 각 버킷에 대한 설명을 제공
        clean()
        input(Mbukkitexplanation)
        clean()
    else:  # Wrong Input
        clean()
        print(Mbukkitselectionerror)
clean()

while True:  # 원하는 서버 버전을 선택 TODO
    ServerVersion = input(Mbukkitversionselection)
    if ServerVersion in Lversionexist:
        break
    clean()
    print(Mserverversiondoesnotexists)
clean()

while True:  # 버킷 다운로드 TODO
    Directory = input(Mserverdirectory)
    if Directory == '':
        Directory = 'C:'.replace(' ', '')
    clean()
    InstallationDirectory = Directory + '\Minecraft_Server_' + ServerVersion
    system('mkdir ' + InstallationDirectory)
    try:
        print('확인을 위해 테스트 파일을 다운로드 하고 있습니다.')
        urllib.request.urlretrieve('https://bit.ly/3fs4fBA', InstallationDirectory + '\Logo.png')
        break
    except (FileNotFoundError, PermissionError):
        print('[오류] 파일 경로가 올바르지 않습니다.')
    except urllib.error.URLError:
        print('[오류] 인터넷에 연결할 수 없습니다.')
clean()
print('이제 버킷 파일을 다운로드 하겠습니다. 다운로드 경로는 '+InstallationDirectory+'입니다.')
print('버킷 파일을 다운로드하는 중 입니다. 이 단계는 사용자의 인터넷 환경에 따라 최대 수분 소요될 수 있습니다.')
Location = Lversionexist.index(ServerVersion)
if BukkitName == 'Vanilla':
    url = ('https://bit.ly/'+Lvanillalinks[Location])

urllib.request.urlretrieve(url, InstallationDirectory +('\ '.replace(' ', ''))+'Server.jar')
clean()
print('파일 다운로드를 완료했습니다. 버킷을 설치합니다.')
system('cd '+InstallationDirectory+'\njava -Xms1G -Xmx2G -jar Server.jar')
input('aaa')
'''
url = 'https://papermc.io/api/v2/projects/paper/versions/'+version+'/builds/'+str(build)+'/downloads/paper-'+version+'-'+str(build)+'.jar'
system('mkdir '+directory+'\AutoBukkitInstallerTemp')
urllib.request.urlretrieve(url, directory+'\AutoBukkitInstaller\Paper_'+version)
'''
