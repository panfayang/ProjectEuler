for i in range(1,500):
	for j in range(1,500):
		if i**2 + j**2 == (1000-i-j)**2:
			print i*j*(1000-i-j)