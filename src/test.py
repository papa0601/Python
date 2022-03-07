''''
import urllib.request


urllib.request.urlretrieve('https://bit.ly/3fs4fBA', 'C:\WhaleDownloadTemp\Logo.png')
'''

# Lversionexist = ['1.18.1', '1.17.1', '1.16.5', '1.12.2', '1.10.2', '1.8.9', '1.7.10', '1.5.2']
# tell = list(reversed(Lversionexist))
# print(tell)
# Location = Lversionexist.index('1.5.2')
# print(Lversionexist[Location])

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