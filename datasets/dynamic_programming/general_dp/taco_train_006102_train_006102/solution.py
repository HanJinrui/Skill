(n, N) = map(int, input().split())

def add(a, b, N=N):
	return (a + b) % N

def mult(a, b, N=N):
	return a * b % N

def div(a, b, N=N):
	return mult(a, pow(b, N - 2, N))

class Cache(object):

	def __init__(self, f, cache_condition=None):
		if cache_condition is None:
			cache_condition = lambda x: True
		self.cache_condition = cache_condition
		self.f = f
		self.d = dict()

	def add(self, *args):
		self.d[args] = self.f(*args)

	def __call__(self, *args):
		if self.cache_condition(args):
			if args not in self.d:
				self.add(*args)
			return self.d[args]
		else:
			return self.f(*args)

	@classmethod
	def cache(cls, cache_condition=None):

		def decorator(f):
			return cls(f, cache_condition)
		return decorator
cache = Cache.cache

class Cache_Generator(Cache):

	def add(self, *args):
		self.d[args] = list(self.f(*args))
cache_generator = Cache_Generator.cache

class Factorial(object):

	def __init__(self, nmax):
		self.data = [0] * nmax
		self.data[0] = 1
		for i in range(1, nmax):
			self.data[i] = mult(self.data[i - 1], i)

	def __call__(self, i):
		return self.data[i]
factorial = Factorial(n)

def n_choose_k(n, k):
	num = factorial(n)
	denom = mult(factorial(n - k), factorial(k))
	return (num, denom)

def combinatorics(n_nodes, partition):
	symmetry_factor = 1
	old_p = None
	count_p = 0
	num = factorial(n_nodes - 1)
	denom = factorial(n_nodes - 1 - sum(partition))
	for p in partition:
		if p == old_p:
			count_p += 1
			symmetry_factor = mult(symmetry_factor, count_p)
		else:
			old_p = p
			count_p = 1
		num = mult(num, ntrees(p))
		denom = mult(denom, factorial(p - 1))
	ret = div(num, mult(denom, symmetry_factor))
	return (ret, symmetry_factor)
top = min(n // 2, 100)

@cache_generator(lambda x: x[0] < top and x[1] < top)
def __partition(sub_tree_max_size, n_nodes):
	yield []
	for i in range(3, min(n_nodes, sub_tree_max_size) + 1):
		for j in _partition(i, n_nodes - i):
			yield ([i] + j)

def _partition(sub_tree_max_size, n_nodes):
	if n_nodes == 0 or sub_tree_max_size == 0:
		yield []
	elif n_nodes == 1:
		yield []
	elif sub_tree_max_size == 1:
		yield []
	else:
		for j in __partition(sub_tree_max_size, n_nodes):
			yield j

def partition(n_nodes):
	return _partition((n_nodes - 1) // 2, n_nodes - 1)

def mylen(x):
	return sum((1 for _ in x))

@cache()
def ntrees(n_nodes):
	if n_nodes == 2:
		return 0
	c = 0
	for p in partition(n_nodes):
		(n, s) = combinatorics(n_nodes, p)
		c = add(c, n)
	return mult(n_nodes, c)
print(ntrees(n))
