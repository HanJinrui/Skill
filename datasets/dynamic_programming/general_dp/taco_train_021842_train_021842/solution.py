def max_len(n, s1, s2):
	longest = 0
	length = len(s1)
	for i0 in range(-length + 1, length):
		s = 0
		m = n
		if i0 > 0:
			i = i0
			j = 0
		else:
			i = 0
			j = -i0
		while i < length and j < length:
			if s1[i] == s2[j]:
				s += 1
				if s > longest:
					longest = s
			elif m == 0:
				while s1[i - s] == s2[j - s]:
					s -= 1
			else:
				m -= 1
				s += 1
				if s > longest:
					longest = s
			i += 1
			j += 1
	return longest
t = int(input())
for _ in range(t):
	(n, s1, s2) = input().split(' ')
	n = int(n)
	full_n = n
	print(max_len(n, s1, s2))
