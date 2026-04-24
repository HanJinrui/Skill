q = input()
a = list(map(int, input().split()))
s = 0
w = 0
for (i, j) in zip(a, sorted(a)):
	s += j - i
	w += not s
print(w)
