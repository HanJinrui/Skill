for i in range(int(input())):
	n = int(input())
	s = input()
	if n % 2 == 1:
		print('NO')
	else:
		d = {}
		for i in s:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		d = dict(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))
		if max(d.values()) > n // 2:
			print('NO')
		else:
			ans = ''
			for i in d:
				ans += i * d[i]
			print('YES')
			final = ans[:n // 2]
			res = ans[n // 2:][::-1]
			print(final + res)
