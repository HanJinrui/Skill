T = int(input())

def calc(w):
	w -= 1
	ans = 1
	t = 10
	d = 1
	while t - 1 <= w:
		ans += t // 10 * 9 * d
		d += 1
		t *= 10
	return ans + d * (w - t // 10 + 1)

def solve(S):
	ans = []
	for K in range(1, len(S) + 1):
		if ans != []:
			break
		for N in range(K):
			sub = S[N:N + K]
			if sub[0] == '0':
				continue
			v = w = int(sub)
			guess = sub
			if N > 0:
				guess = (str(v - 1) + guess)[-N - K:]
			if guess != S[0:N + K]:
				continue
			i = N + K
			good = True
			while good and len(guess) < len(S):
				v += 1
				guess = guess + str(v)
				while good and i < len(S) and (i < len(guess)):
					if S[i] != guess[i]:
						good = False
						break
					i += 1
			if good:
				ans.append(calc(w) - N)
	return ans
for tc in range(T):
	S = input().strip()
	ans = []
	ans.extend(solve(S))
	ans.append(calc(int('1' + S)) + 1)
	print(min(ans) % 1000000007)
