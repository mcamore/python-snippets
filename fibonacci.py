#!/usr/bin/env python3

# Author: mcamore (mmco94@live.com)
# Usage: python fibonacci.py [numer_of_iterations]
# Example: "python fibonnaci.py 5" returns "[0, 1, 1, 2, 3, 5]"
# Requires Python 3.x

from sys import argv
def fibonacci():
	fibonacciList = [0, 1]
	try:
		for i in range(1, int(argv[1])):
			sumatory = fibonacciList[i - 1] + fibonacciList[i]
			fibonacciList.append(sumatory)
		print(fibonacciList)
	except IndexError:
		print("\nError: Introduce the number of iterations.\nExample: fibonacci.py 10")
	except ValueError:
		print("\nError: Number of iterations must be a integer value.\nExample: fibonacci.py 10")
	except:
		print("\nUknown error...")

if __name__ == "__main__": fibonacci()
