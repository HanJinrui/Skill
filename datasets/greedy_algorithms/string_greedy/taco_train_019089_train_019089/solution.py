from collections import Counter
s = Counter(sorted(list(input())))
odds = [key for key in s if s[key] % 2]
l = len(odds)
for i in range(l // 2):
	s[odds[i]] += 1
	s[odds[l - i - 1]] -= 1
mid = odds[l // 2] if l % 2 else ''
ans = ''.join([key * (s[key] // 2) for key in s])
print(ans + mid + ans[::-1])
