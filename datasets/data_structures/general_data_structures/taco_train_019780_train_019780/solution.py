def inverted_swap(s):
	"""
	>>> inverted_swap('h')
	'h'
	>>> inverted_swap('he')
	'he'
	>>> inverted_swap('hpel')
	'help'
	>>> inverted_swap('ctosnet')
	'contest'
	"""
	len_s = len(s)
	if len_s % 2 == 0:
		return s[::2] + s[-1::-2]
	else:
		return s[::2] + s[-2::-2]


if __name__ == "__main__":
	k = int(input())
	s = input()
	orig_s = s
	cycle_duration = 0
	while k:
		s = inverted_swap(s)
		k -= 1
		cycle_duration += 1
		if s == orig_s:
			k = k % cycle_duration
	print(s)
