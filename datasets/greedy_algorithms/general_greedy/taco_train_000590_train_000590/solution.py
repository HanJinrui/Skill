from collections import Counter
original = s = input()
counter = Counter(s)
for k in counter:
	counter[k] //= 2
word = ''
while len(word) < len(original) // 2:
	for c in sorted(counter.keys()):
		i = s.rfind(c)
		left = Counter(s[:i + 1])
		if all((k in left and left[k] >= counter[k] for k in counter)):
			word += c
			s = s[:i]
			counter[c] -= 1
			if counter[c] == 0:
				del counter[c]
			break
print(word)
