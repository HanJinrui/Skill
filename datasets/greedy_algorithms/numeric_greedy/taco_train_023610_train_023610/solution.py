n = int(input())
iv = [int(x) for x in input().split()]
(s, st) = (set(range(1, n + 1)), [])
for i in range(n):
	if iv[i] not in s:
		st.append(i)
	s.discard(iv[i])
for i in st:
	iv[i] = s.pop()
print(*iv)
