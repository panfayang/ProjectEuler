triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

list_tri = triangle.split("\n")
finalList = []
for i in list_tri:
    for j in i.split(" "):
        finalList.append(int(j))

##print finalList
pos = []
dic = {}
for i in range(15):
    for j in range(i+1):
        pos.append((i,j))

for i,j in zip(pos,finalList):
    dic[i] = j
##print dic

class binary(object):
    def __init__(self,node):
        self.node = node
        self.dic = dic

    def value(self):
        return self.dic[self.node]

    def l(self):
        new = (self.node[0]+1,self.node[1])
        if new in self.dic:
            return self.dic[new]
        else:
            return

    def r(self):
        new = (self.node[0]+1,self.node[1]+1)
        if new in self.dic:
            return self.dic[new]
        else:
            return

    def findMax(self):
        a = 0
        if self.l() > self.r():
            dic[self.node] = self.l() + self.value()
        else:
            dic[self.node]= self.r() + self.value()
        return dic[self.node]

dic2 = {}
n = binary((13,0))
print n.r()

for i in range (100,-1,-1):
    for j in range(i+1):
        n = binary((i,j))
        m = n.findMax()
print m
