n = int(input()) // 3
s = input()
a = [n - s.count(str(i)) for i in range(3)]
for i in [0, 2, 1]:
	if a[i] > 0:
		for j in range(3):
			if a[j] < 0:
				r = min(a[i], abs(a[j]))
				a[i] -= r
				a[j] += r
				if i > j:
					s = s[::-1].replace(str(j), str(i), r)[::-1]
				else:
					s = s.replace(str(j), str(i), r)
print(s)
