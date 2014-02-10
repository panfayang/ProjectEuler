n = open('names.txt','r')
names = n.read()
nameList = names.split('","')
nameList.sort()
print type(nameList.index('COLIN'))
##nameList.split(",")

def score(stringah):
    num = 0
    for i in stringah:
        num += ord(i)-64
    return num
print type(score('COLIN'))

def nameScore(stringba):
    return score(stringba)*(nameList.index(stringba)+1)
##    return final

print nameScore('COLIN')

scoreList = 0
for i in nameList:
    scoreList += nameScore(i)

print scoreList

