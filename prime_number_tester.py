import time
import timeit
import threading

# Import the prime number testers (PNTs)
from naive_pnt import naive_pnt
from improved_pnt import improved_pnt
from other_improved_pnt import other_improved_pnt


# Serves as padding to prevent incorrect input types
def pnt_test_wrapper(function, number):
	if type(number) is int:
		function(number)
	else:
		raise TypeError("number is not int")

class BenchmarkThread(threading.Thread):
	def __init__(self, function_pointer, number):
		threading.Thread.__init__(self)
		self.function_pointer = function_pointer
		self.number = number

	def run(self):
		print(self.function_pointer.__name__ + " has started.\n")
		start_time = timeit.default_timer()
		result = pnt_test_wrapper(self.function_pointer, self.number)
		elapsed = timeit.default_timer() - start_time

		print(
			"{} is finished.\n".format(self.function_pointer.__name__)
			+ "{} is{} prime\n".format(self.number, ("" if result else " not"))
			+ "Time elapsed: {}s\n".format(elapsed)
		)


def main():
	# take number from user
	stringinput = input("Enter a number: ")
	number = int(stringinput)
	print("The number you have entered is {}\n".format(number))

	# wait for 1 second
	time.sleep(1)

	thread1 = BenchmarkThread(naive_pnt, number)
	thread2 = BenchmarkThread(improved_pnt, number)
	thread3 = BenchmarkThread(other_improved_pnt, number)

	thread1.start()
	thread2.start()
	thread3.start()


if __name__ == "__main__":
	main()
