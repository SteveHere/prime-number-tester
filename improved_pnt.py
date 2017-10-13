# Improved prime number tester
# Immediately after the naive version, people would know that
#  they would only need to test up to the square root of n to prove it is prime,
#  because root of n * root of n == n .
# This reduces the number of elements needed to the root of n.
# They would also try to see if it was 2 or a factor of 2 immediately
# They would also know that even numbers are off the table
#  , and thus only increment the range by 2, halving that list.

# Number of elements needed: (square root of n)/2


def improved_pnt(number):
	# Prime testing begins here
	if number is 2:
		return True
	if number % 2 == 0:
		return False
	if number > 1:
		# check for factors up to square root of number
		for i in range(3, int(number ** 0.5) + 1, 2):
			if (number % i) == 0:
				return False
		return True
	# if number number is less than
	# or equal to 1, it is not prime
	return False