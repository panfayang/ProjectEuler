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
        
        for i in primes(10000):
                b = 0
                if n == 1:
                        break
                while n%i == 0:
                        n = n/i
                        b+=1
                num = num*(b+1)
        return num



def triangle(n):
        return (1+n)*n/2
##print checkFactor(triangle(7))
def find500(n):
        if checkFactor(triangle(n))>500:
                return n,triangle(n)
        else:
                return find500(n+1)

print find500(1)
