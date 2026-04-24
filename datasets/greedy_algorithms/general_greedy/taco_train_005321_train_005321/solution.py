from collections import *
t = 'RPSR'
for s in [*open(0)][1:]:
	print(t[t.find(Counter(s).most_common()[0][0]) + 1] * (len(s) - 1))
