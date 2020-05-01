num = int(input())
adict = dict()
bdict = dict()
for i in range(num):
    sinonim = list(map(str, input().split()))
    adict[sinonim[0]] = sinonim[1]
    bdict[sinonim[1]] = sinonim[0]
lastWord = str(input())
try:
    print(adict[lastWord])
except:
    print(bdict[lastWord])
