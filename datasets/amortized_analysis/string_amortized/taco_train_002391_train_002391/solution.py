from collections import Counter
for _ in range(int(input())):
	(_, s1, s2) = (input() for _ in range(3))
	odd = [p for (p, v) in Counter((frozenset((x, y)) for (x, y) in zip(reversed(s1), s2))).items() if v % 2]
	print(('NO', 'YES')[len(odd) == 0 or (len(odd) == 1 and len(odd[0]) == 1)])
