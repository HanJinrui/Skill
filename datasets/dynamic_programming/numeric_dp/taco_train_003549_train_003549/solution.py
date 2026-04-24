import fractions;
from functools import reduce

N,K = list(map(int, input().split()));

raju = list(map(int, input().split()));
rani = list(map(int, input().split()));

raju.append(360);

gcd = reduce(fractions.gcd, raju);

for i in rani:
	if (0 == i%gcd):
		print("YES");
	else:
		print("NO");
