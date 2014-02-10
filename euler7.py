

def checkprime(p):
	n = []
	for m in range(2,int(p**0.5)+1):
		if p % m ==0:
			break
			return False
		elif m == int(p**0.5):
			return True			
			
def prime(no):
	m = 0
	
	for i in range(2, 1000000):
		if checkprime(i) is True:
			m = m + 1
		elif no == m:
			break
	return (i-1)

print checkprime(5)

print prime(9999)

# 
# 
# m = 0
# for i in range(2, 20):
# 	if checkprime(i) is True:
# 		m = m + 1
# 		print i
# 			
# print m


