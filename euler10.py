def checkprime(n):
	for i in range(2, int(n**0.5)+2):
		if n % i == 0:
			break
			return False
		elif i == int(n**0.5)+1:
			return True

# print checkprime(15)

n = []

for j in range(2,2000000):
	if checkprime(j) is True:
		n.append(j)

print sum(n)+2