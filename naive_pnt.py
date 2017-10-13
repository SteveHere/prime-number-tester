# Naive prime number tester
# How people would immediately write a prime number tester
# Incredibly inefficient, only coded when in a quick rush to try something.

# Number of elements needed to test: n , where n = input


def naive_pnt(number):
	# Prime testing begins here
	if number > 1:
		# check for factors up to square root of number
		for i in range(2, int(number)):
			if (number % i) == 0:
				return False
		else:
			return True
	# if number number is less than
	# or equal to 1, it is not prime
	else:
		return False