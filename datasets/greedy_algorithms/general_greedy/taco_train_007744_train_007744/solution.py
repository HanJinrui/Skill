n = int(input())
w = sorted(map(int, input().split()))
(t, c) = (0, -10)
for x in w:
	if c + 4 < x:
		t += 1
		c = x
print(t)
