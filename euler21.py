import sys
sys.setrecursionlimit(1000000000)

def primes(n):
        if n==2: return [2]
        elif n<2: return []
        s=range(3,n+1,2)
        mroot = n ** 0.5
        half=(n+1)/2-1
        i=0
        m=3
        while m <= mroot:
                if s[i]:
                        j=(m*m-3)/2
                        s[j]=0
                        while j<half:
                                s[j]=0
                                j+=m
                i=i+1
                m=2*i+3
        return [2]+[x for x in s if x]



def checkFactor(n):
        num = 1
        b = []
        for i in range(2,5000):
                if i>n**0.5:
                        break
                else:
                        if n%i == 0:
                                b.append(i)
                                if i != n/i:
                                        b.append(n/i)
        for i in b:
                num += i
        return num

dic = {}
for i in range(10000):
        dic[i] = checkFactor(i)

lis = []
for i in dic.keys():
        for j in dic.keys():
                if j == dic[i] and i == dic[j] and j != dic[j]:
                        lis.append(j)
                        lis.append(i)
                        break

total = 0
for i in lis:
        total += i
print total/2
##print dic[4]
##print dic[220]
