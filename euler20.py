n = 1
for i in range(1,101):
    n = n*i

summ = 0
for i in str(n):
    summ += int(i)

print summ
