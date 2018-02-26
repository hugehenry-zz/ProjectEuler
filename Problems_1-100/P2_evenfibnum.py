def evenfib(upp_lim):
	# Return the sum of all even fibonacci numbers from 1 to upp_lim.
	tot_sum = 0
	# Save the last two fib numbers
	fib_a = 0
	fib_b = 1

	for i in range(upp_lim):
		if i == fib_a + fib_b: # Have you found a third fib number?
			fib_a, fib_b, i = fib_b, fib_a + fib_b, fib_a + fib_b
			if i % 2 == 0: # Save the even numbers
				tot_sum += i

	return tot_sum

print(evenfib(4000000))
