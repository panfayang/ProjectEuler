def palin(x):
	if len(x)==1:
		return True
	elif len(x)==0:
		return True
	elif x[0] == x[-1]:
		x.remove(x[0])
		x.pop()
		return palin (x)
	else:		
		return False
# 	elif x == []:
# 	y = x
# 	print y
# 	x.reverse()
# 	print x
# 	
# 	print ''.join(y)
# 	b = ''.join(x)
# 	print b
# 	if a == b:
# 		return True
# 	else:
# 		return False
# 
print palin(['1','2','1','2','1','3'])

n = []

for i in range(100,1000):
	for j in range (100,1000):
		if palin(list(str(i*j))) is True:
			n = n + [i*j]
print max(n)
	

# a = 1234
# b = list(str(a))
# print b