from re import findall
from calendar import monthrange
from collections import defaultdict
S = input()
bag = defaultdict(int)
for s in findall('(?=(\\d\\d-\\d\\d-201[3-5]))', S):
	(d, m, y) = map(int, s.split('-'))
	if 1 <= m <= 12 and 1 <= d <= monthrange(y, m)[1]:
		bag[s] += 1
print(max(bag, key=bag.get))
