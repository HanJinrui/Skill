(a, b, p) = map(int, input().split())

def k(x):
	return bool(int(x) % p)
(x, y) = (list(map(k, input().split())), list(map(k, input().split())))
print(x.index(True) + y.index(True))
