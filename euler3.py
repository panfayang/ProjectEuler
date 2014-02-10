# def findprime(x):
# 	n = []
# 	for i in range(2,x/7):
# 		if x % i ==0 and checkprime(i) is True:
# 			n.append(i)
# 	return n
# 
# 
# def checkprime(p):
# 	n = []
# 	for m in range(2,p /7):
# 		if p % m ==0:
# 			n.append(m)
# 	if n == []:
# 		return True
# 	else:
# 		return False
# 
# print checkprime(23)
# print findprime(600851475143)



def primefactor(x):
	n = []
	for i in range(2,int(x**0.5)):
		if x% i == 0:
			x = x / i
			print x
			n.append(i)
			break
	return n

print primefactor(6857)