n = int(input())
arr = sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1])
ans = [str(x[0]) for x in arr]
q = ['YES', ' '.join(ans)]
for i in range(n - 1):
	if arr[i][1] == arr[i + 1][1]:
		(ans[i], ans[i + 1]) = (ans[i + 1], ans[i])
		q.append(' '.join(ans))
		if len(q) > 3:
			break
print('\n'.join(q) if len(q) > 3 else 'NO')
