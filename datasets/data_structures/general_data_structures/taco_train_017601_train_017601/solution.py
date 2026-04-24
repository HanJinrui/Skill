for _ in range(int(input())):
	s = input()
	ans = set()
	for i in range(len(s)):
		ones = 0
		count = 0
		for j in range(i, len(s)):
			if s[j] == '1':
				ones += 1
			if ones & 1:
				count += 1
			ans.add((j - i + 1, ones, count))
	print(len(ans))
