modulus = 10 ** 9 + 7

def itable_to_multiset(s):
	rv = {}
	for x in s:
		rv[x] = rv.get(x, 0) + 1
	return rv

def answer(b, finish, start, m):
	assert len(start) == len(finish)
	rv = 0
	for (s, f) in zip(start, finish):
		rv *= b
		rv %= m
		rv += f - s
	return rv % m
t = int(input())
for _ in range(t):
	(n, b) = (int(x) for x in input().split())
	as_ = [int(x) for x in input().split()]
	dig_freqs = itable_to_multiset(as_)
	all_digs = set(range(b))
	missing = all_digs - set(dig_freqs.keys())
	if len(missing) == 0:
		print(0)
		continue
	done = False
	max_missing = max(missing)
	for (dig, idx) in zip(reversed(as_), range(1, n + 1)):
		dig_freqs[dig] -= 1
		if dig_freqs[dig] == 0:
			missing.add(dig)
			if dig > max_missing:
				max_missing = dig
		if len(missing) > idx or dig == b - 1 or (len(missing) == idx and dig >= max_missing):
			continue
		if len(missing) < idx:
			new_dig = dig + 1
		else:
			new_dig = min(missing.intersection(range(dig + 1, b)))
		if new_dig in missing:
			missing.remove(new_dig)
		missing = list(missing)
		missing.sort()
		print(answer(b, [new_dig] + [0] * (idx - 1 - len(missing)) + missing, as_[-idx:], modulus))
		done = True
		break
	if done:
		continue
	ans_len = max(n + 1, b)
	print(answer(b, [1] + [0] * (ans_len + 1 - b) + list(range(2, b)), [0] * (ans_len - n) + as_, modulus))
