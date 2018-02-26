def mult35(upp_lim):
	# Return the sum all the multiples of 3 and 5 from 0 to upp_lim.
	tot_sum = 0
	for i in range(upp_lim):
		if i % 3 == 0 or i % 5 == 0:
			tot_sum += i

	return tot_sum

print(mult35(1000))
