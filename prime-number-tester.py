import time
import timeit
import threading


class BenchmarkThread(threading.Thread):
	def __init__(self, function_pointer, number):
		threading.Thread.__init__(self)
		self.function_pointer = function_pointer
		self.number = number

	def run(self):
		print(self.function_pointer.__name__ + " has started.\n")
		start_time = timeit.default_timer()
		result = self.function_pointer(self.number)
		elapsed = timeit.default_timer() - start_time
		result = "{} is finished.\n".format(self.function_pointer.__name__)\
		         + "{} is{} prime\n".format(str(self.number), ("" if result else " not"))\
		         + "Time elapsed: {}s\n".format(str(elapsed))
		print(result)


def main():
	# take number from user
	stringinput = input("Enter a number: ")
	number = int(stringinput)
	print("The number you have entered is " + str(number))

	# wait for 1 second
	time.sleep(1)

	thread1 = BenchmarkThread(naive_prime_number_test, number)
	thread2 = BenchmarkThread(improved_prime_number_test, number)

	thread1.start()
	thread2.start()


# Naive prime number test
def naive_prime_number_test(number):
	if type(number) is int:
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
	else:
		raise TypeError("number is not int")


# Improved prime number test
def improved_prime_number_test(number):
	if type(number) is int:
		# Prime testing begins here
		if number is 2:
			return True
		elif number > 1:
			# check for factors up to square root of number
			for i in range(3, int(number ** 0.5), 2):
				if (number % i) == 0:
					return False
			else:
				return True
		# if number number is less than
		# or equal to 1, it is not prime
		else:
			return False
	else:
		raise TypeError("number is not int")


if __name__ == "__main__":
	main()
