def smallestSubsequence(s, k):
	toRem = len(s) - k
	ind = 0
	while ind < len(s) - 1 and toRem > 0:
		if s[ind] > s[ind + 1]:
			s = s[:ind] + s[ind + 1:]
			toRem -= 1
			ind -= 1
			if ind < 0:
				ind = 0
		else:
			ind += 1
	s = s[:k]
	return s
for ii in range(int(input())):
	s = input()
	k = int(input())
	print(smallestSubsequence(s, k))
