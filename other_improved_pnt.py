# Other improved prime number tester
# Another way people could improve the speed of the naive version
#  is to just try and test against the primes themselves.
# After checking for if the number's 2, 3, or has one of them
#  as their factors, they would notice that the primes would be
#  in the form of 6k - 1 or 6k + 1.
# Example: 5 = 6(1) - 1, 43 = 6(7) + 1, and 89 = 6(15) - 1
# However, some of them are not primes, like 25 = 6(4) + 1, 55 = 6(9) + 1,
#  and 85 = 6(14) + 1, so a check to see if they are a factor of 5 would be needed
# With the same k, these numbers would be 2 apart,
#  and a number in 6k + 1 is only 4 away from the next 6k - 1,
#  because 6(k + 1) - 1
#           = 6k + 6 - 1
#           = 6k + 5
#           = 6k + 1 + 4,
#  so they would need to iterate by 2 and 4 alternately


from itertools import cycle


# An extension of range for alternating steps
# Thanks to mgilson from this Stack Overflow answer:
# https://stackoverflow.com/a/39241588/4688876
def fancy_range(start, stop, steps=(1,)):
    steps = cycle(steps)
    val = start
    while val < stop:
        yield val
        val += next(steps)


def other_improved_pnt(number):
	# Checks if they are 2 or 3, or their factors
	if number == 2: return True
	if number == 3: return True
	if number % 2 == 0: return False
	if number % 3 == 0: return False

	# Does the check against primes using 6k + 1 and 6k - 1
	#  mentioned earlier
	for i in fancy_range(5, int(number ** 0.5) + 1, (2, 4)):
		# Goes to the next number if it's a factor of 5 and not 5
		if i % 5 == 0 and i is not 5:
			continue
		if number % i == 0:
			return False
	return True