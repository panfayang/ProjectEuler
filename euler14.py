def count(n):
    a = 1
    while n !=1:
        if n%2 == 0:
            n = n/2
            a += 1
        else:
            n = 3*n +1
            a += 1
    return a

def findMax(n):
    a = 0
    c = 0
    for i in range(1,n):
        b = count(i)
        if b>a:
            a = b
            c = i
        else: pass
    return c,a

print findMax(1000000)
