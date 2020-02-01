# function to check if the number is 
# prime or not 
def isPrime(n) : 
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True

	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True

# print all prime numbers 
# less than equal to N 
def printPrime(n): 
	for i in range(2, n + 1): 
		if isPrime(i): 
			print (i, end =" ") 

n = 1000		
printPrime(n) 
