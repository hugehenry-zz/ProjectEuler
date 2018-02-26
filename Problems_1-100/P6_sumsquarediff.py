def sumsq(x):
	# Sums the square and the square of the sum of the numbers in range, and return the difference.
	a_sum = 0
	for i in range(x + 1):
		a_sum += i**2

	
	b_sum = sum(range(0, x + 1))**2

	return b_sum - a_sum

print(sumsq(100))
