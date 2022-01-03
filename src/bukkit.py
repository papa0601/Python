from os import system
import requests
import urllib.request

while True:
    answer = input('[입력] 서버를 열 마인크래프트 버킷의 종류를 선택해주세요.\n'
                   '1.Vanilla\n'
                   '2.CraftBukkit\n'
                   '3.Spigot\n'
                   '4.Paper\n\n'
                   '[각 버킷에 대한 설명을 보려면 0을 입력하세요]\n>>>')  # 버킷의 종류 확인
    if answer == '1':  # Vanilla
        system('cls')
        check = input('[경고] Vanilla 버킷은 플러그인을 지원하지 않습니다. 그래도 계속하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            BukkitName = 'Vanilla'
            break
        system('cls')
    elif answer == '2':  # CraftBukkit
        check = input('[확인] CraftBukkit을 선택하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            BukkitName = 'CraftBukkit'
            break
        system('cls')
    elif answer == '3':  # Spigot
        check = input('[확인] Spigot을 선택하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            BukkitName = 'Spigot'
            break
        system('cls')
    elif answer == '4':  # Paper
        check = input('[경고] 이 프로그램은 아직 Paper버킷의 설치를 완벽히 지원하지 않으며 따라서 사용자가 일부 기능을 수행해야 합니다. 그래도 계속하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            BukkitName = 'Paper'
            break
        system('cls')
    elif answer == '0':  # Show Explanation of Each Bukkit
        system('cls')
        input('[설명]\n1.Vanilla(바닐라) 바닐라 버킷은 수정되지 않은 원본 마인크래프트 서버 프로그램으로 제작사(모장 스튜디오)에서 직접 배포합니다. 그러나 이 종류의 버킷은 플러그인을 지원하지 않습니다.\n'
              '2.CraftBukkit(크래프트버킷) 크래프트버킷은 Vanilla를 수정하여 만들어진 버킷입니다. Vanilla의 버그 수정 및 최적화와 함께 플러그인을 지원합니다.\n'
              '3.Spigot(스피갓) 스피갓은 CraftBukkit를 수정하여 만들어진 버킷입니다. 가장 흔하게 사용되는 버킷으로 CraftBukkit보다 개선되고 최척화된 버킷입니다.\n'
              '4.Paper(페이퍼) 페이퍼는 Spigot에 여러가지 패치를 하여 만들어진 버킷입니다. 매우 빠르고 고성능이지만 많은 패치로 인하여 일부 플러그인과 호환되지 않을 수 있습니다.\n\n'
              '[버킷 선택 페이지로 돌아가려면 Enter를 입력해주세요]')
        system('cls')
    else:  # Wrong Input
        system('cls')
        print('[오류] 각 버킷에 해당하는 선택지의 번호를 입력해주세요.\n')
system('cls')

while True:
    answer = input('[입력] 서버를 열 마인크래프트 버전을 선택해주세요.(1.12.2 ~ 1.18.1)\n[버전을 마지막 자리를 제외한 숫자로 입력해주세요. 자동으로 해당 버전의 최신 빌드가 선택됩니다. 예) 1.16 --> 1.16.5 / 1.17 --> 1.17.1\n\n>>>')
    if answer == '1.18':
        check = input('[확인] 서버의 버전을 1.18.1로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.18.1'
            break
        system('cls')
    elif answer == '1.17':
        check = input('[확인] 서버의 버전을 1.17.1로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.17.1'
            break
        system('cls')
    elif answer == '1.16':
        check = input('[확인] 서버의 버전을 1.16.5로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.16.5'
            break
        system('cls')
    elif answer == '1.15':
        check = input('[확인] 서버의 버전을 1.15.2로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.15.2'
            break
        system('cls')
    elif answer == '1.14':
        check = input('[확인] 서버의 버전을 1.14.4로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.14.4'
            break
        system('cls')
    elif answer == '1.13':
        check = input('[확인] 서버의 버전을 1.13.2로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.13.2'
            break
        system('cls')
    elif answer == '1.12':
        check = input('[확인] 서버의 버전을 1.12.2로 하시겠습니까?(y/n)\n\n>>>')
        if check == 'y':
            Version = '1.12.2'
            break
        system('cls')
    else:
        system('cls')
        print('[오류] 버전을 올바르게 입력해주세요. (1.16.5[X] / 1.16[O])')
system('cls')
while True:
    print('[경고] 입력이 잘 못되어 오류가 발생할 가능성이 높은 부분입니다. 입력 예시를 확인하시고 답변을 다시 한 번 확인해주세요.')
    Directory = input('[입력] 마인크래프트 버킷을 설치할 폴더의 경로를 입력해주세요. 이것이 무엇인지 잘 모르겠다면 공백으로 비워두세요, 자동으로 C:\Games에 설치됩니다. 예)C:\Games \n[알림] 다음 단계에서 버킷을 담을 빈 폴더가 자동으로 생성되니 참고해주세요.\n\n>>>')
    if Directory == '':
        Directory = 'C:\Games'
    system('cls')
    FolderName = '\MinecraftServer_'+Version+'_'+BukkitName
    system('mkdir '+Directory+FolderName)


'''
url = 'https://papermc.io/api/v2/projects/paper/versions/'+version+'/builds/'+str(build)+'/downloads/paper-'+version+'-'+str(build)+'.jar'
system('mkdir '+directory+'\AutoBukkitInstallerTemp')
urllib.request.urlretrieve(url, directory+'\AutoBukkitInstaller\Paper_'+version)
'''