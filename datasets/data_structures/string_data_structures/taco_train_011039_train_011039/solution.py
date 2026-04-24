def remAnagram(str1, str2):
	c = 0
	ab = list(set(str1 + str2))
	for i in ab:
		c += abs(str1.count(i) - str2.count(i))
	return c
