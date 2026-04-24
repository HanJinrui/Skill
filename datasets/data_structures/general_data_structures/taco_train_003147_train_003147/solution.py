def main():
	N = int(input().strip())
	ps = list(map(int, input().split()))
	s = []
	maxDay = 0
	for p in ps:
		d = 0
		while s and p <= s[-1][0]:
			d = max(d, s.pop()[1])
		if not s:
			d = 0
		else:
			d += 1
		s.append((p, d))
		maxDay = max(maxDay, d)
	print(maxDay)
main()
