from collections import Counter
from string import ascii_lowercase as al
for _ in range(int(input())):
	c = Counter(input().strip())
	print(" ".join(sorted(al[::-1], key=lambda x:c[x])))
