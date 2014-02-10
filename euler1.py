

n=[]

for i in range(1000):
	if i % 3 == 0:
		n.append(i)
	elif i % 5 == 0:
		n.append(i)
m = set(n)
k = list(m)

sum= 0

for l in range(len(k)):
	sum = sum + k[l]

print sum