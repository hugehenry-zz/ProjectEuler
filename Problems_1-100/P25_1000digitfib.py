import time

def fib1000(nr_len, upp_lim, yn):
	# Return the index of the first fib number that's 1000 digits long
	# nr_len, length of number
	# upp_lim, upper limit
	# yn, enter 1 to return index AND number
	
	# Start the timer
	timer_start = time.clock()

	fib_a = 0 # Save the last two fib numbers
	fib_b = 1
	fib_i = 1 # Fib number index

	for i in range(upp_lim + 1):
		if i == fib_a + fib_b: # Have you found a third fib number?
			if len(str(i)) == nr_len:

				if yn:
					return ("Index: " + str(fib_i) + 
							"\nNumber: " + str(i) +
							"\nElapsed time: " + str(time.clock() - timer_start) + " s.")

				return ("Index: " + str(fib_i) + 
						"\nElapsed time: " + str(time.clock() - timer_start) + " s.")

			fib_i += 1

			# Let i skip non fib numbers
			fib_a, fib_b, i = fib_b, fib_a + fib_b, fib_a + fib_b

	return ("No matching number found in the first " + str(upp_lim) + " numbers." +
			"\nElapsed time: " + str(time.clock() - timer_start) + " s.")

print(fib1000(50, 1000000000000, True))