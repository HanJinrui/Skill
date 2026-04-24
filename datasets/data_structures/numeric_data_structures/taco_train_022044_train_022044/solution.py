a = int(input())
s = input()
d = {}
for i in range(len(s)):
	for j in range(i, len(s)):
		if j == i:
			t = int(s[j])
		else:
			t += int(s[j])
		d[t] = d.get(t, 0) + 1
if a == 0:
	if 0 in d:
		cnt_pairs = len(s) * (len(s) + 1) // 2
		print(d[0] * cnt_pairs + d[0] * (cnt_pairs - d[0]))
	else:
		print(0)
else:
	c = 0
	for f in d:
		if f != 0 and a % f == 0 and (a // f in d):
			c += d[f] * d[a // f]
	print(c)
