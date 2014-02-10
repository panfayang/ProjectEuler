def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	else:
		return fib(n-1)+fib(n-2)


def findfib(x):
	while fib(x)<4000000:
		x = x+1
	return x
sum =0

for i in range(33):
	if fib(i) % 2 ==0:
		sum = sum + fib(i)

print sum