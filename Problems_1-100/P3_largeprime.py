def largeprime(prime):
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 
			29, 31, 37, 41, 43, 47, 53, 59, 61,
			67, 71, 73, 79, 83, 89, 97, 101]

	not_found = True


	for i in primes:
		print(1)
		if prime in primes:
			print(2)
			return prime
		prime = prime / i
		print(3)

print(largeprime(13195))
