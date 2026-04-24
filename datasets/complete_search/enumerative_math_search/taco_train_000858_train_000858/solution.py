import itertools
import math

class Main:

	def __init__(self):
		iterable = self.__standard()
		self.__solution(iterable)

	def __solution(self, iterable):
		(cases,) = map(int, next(iterable).split())
		for _test in range(cases):
			(remainder, prime) = map(int, next(iterable).split())
			sqrt5 = self.__sqrt(5, prime)
			normalized = remainder * sqrt5 % prime
			half = pow(2, prime - 2, prime)
			phi = (1 + sqrt5) * half % prime
			b = -normalized % prime
			D = b * b - 4
			candidates = []
			try:
				d = self.__sqrt(D % prime, prime)
			except ValueError:
				pass
			else:
				candidates.append(((-b + d) * half % prime, 1))
				candidates.append(((-b - d) * half % prime, 1))
			D = b * b + 4
			try:
				d = self.__sqrt(D % prime, prime)
			except ValueError:
				pass
			else:
				candidates.append(((-b + d) * half % prime, 0))
				candidates.append(((-b - d) * half % prime, 0))
			solutions = []
			for (x, category) in candidates:
				for index in self.__logarithm(x, phi, prime, category):
					solutions.append(index)
			try:
				result = min(solutions)
			except ValueError:
				result = -1
			print(result)

	def __logarithm(self, power, base, prime, category):
		basePeriod = self.__period(base, prime)
		powerPeriod = self.__period(power, prime)
		if basePeriod % powerPeriod:
			return
		for index in self.__discreteLogarithm(power, base, prime):
			if index & 1 == category:
				yield index
			else:
				future = index + basePeriod
				if future < prime and future & 1 == category:
					yield future
			return

	def __discreteLogarithm(self, number, base, prime):
		limit = math.ceil(prime ** 0.5)
		lookup = {}
		for small in range(limit):
			lookup.setdefault(pow(base, small, prime), small)
		current = number
		multiplier = pow(base, prime - 1 - limit, prime)
		for large in range(limit):
			try:
				small = lookup[current]
			except KeyError:
				pass
			else:
				yield (limit * large + small)
				return
			current = current * multiplier % prime

	def __sqrt(self, square, prime):
		if not square:
			return 0
		if pow(square, prime - 1 >> 1, prime) != 1:
			raise ValueError()
		(odd, even) = (prime - 1, 0)
		while not odd & 1:
			odd >>= 1
			even += 1
		for generator in range(1, prime):
			if pow(generator, prime - 1 >> 1, prime) != 1:
				break
		else:
			raise AssertionError()
		result = pow(square, odd + 1 >> 1, prime)
		off = pow(square, odd, prime)
		constant = pow(generator, odd, prime)
		remaining = even
		while True:
			forecast = off
			distance = 0
			for distance in range(remaining):
				if forecast == 1:
					break
				forecast = forecast * forecast % prime
			if distance == 0:
				return result
			constroot = pow(constant, 1 << remaining - distance - 1, prime)
			constant = constroot * constroot % prime
			result = result * constroot % prime
			off = off * constant % prime
			remaining = distance

	def __period(self, base, modulo):
		index = modulo - 1
		for (prime, exponent) in self.__factors(index):
			for _iteration in range(exponent):
				test = index // prime
				if pow(base, test, modulo) == 1:
					index = test
				else:
					break
		return index

	def __factors(self, number):
		if not number & 1:
			count = (number ^ number - 1).bit_length() - 1
			number >>= count
			yield (2, count)
		for divisor in itertools.count(3, 2):
			if divisor * divisor > number:
				break
			if not number % divisor:
				number //= divisor
				count = 1
				while not number % divisor:
					number //= divisor
					count += 1
				yield (divisor, count)
		if number > 1:
			yield (number, 1)

	def __test(self):
		yield '4'
		yield '0 11'
		yield '16 19'
		yield '18 19'
		yield '4 19'

	def __standard(self):
		try:
			while True:
				yield input()
		except EOFError:
			pass
Main()
