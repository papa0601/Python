olist = ['1.0', '2.0', '3.0', '3.1', '3.11', 'NT', '95', '98', '2000', 'ME', 'XP', '7', '8', '8.1', '10', '11']
nlist = []
count = int(input('리스트를 불러올 범위를 지정해주세요>>>(1~' + str(len(olist)) + ')>>>')) - 1
for i in range(count + 1):
    nlist.append('')
if count < 0:
    count = 0
elif count > len(olist):
    count = len(olist)
for i in range(count + 1):
    nlist[i] = olist[i]
    print(nlist[i])