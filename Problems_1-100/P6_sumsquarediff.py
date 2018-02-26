def sumsq(x):
	a_sum = 0
	for i in range(x + 1):
		a_sum += i**2

	
	b_sum = sum(range(0, x + 1))**2

	return b_sum - a_sum

print(sumsq(100))