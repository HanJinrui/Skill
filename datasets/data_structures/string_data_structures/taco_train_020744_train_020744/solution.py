def Sandwiched_Vowel(s):
	s = list(s)
	s1 = list('aeiou')
	for i in range(1, len(s) - 1):
		if s[i] in s1:
			if s[i - 1] not in s1:
				if s[i + 1] not in s1:
					s[i] = ''
	return ''.join(s)
