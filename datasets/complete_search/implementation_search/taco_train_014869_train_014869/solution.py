A = list(map(int, input().split()))
score = 0
for i in range(14):
	score = max(score, sum([j for j in [(A[j] if i != j else 0) + A[i] // 14 + (1 if (j + 13 - i) % 14 < A[i] % 14 else 0) for j in range(14)] if j % 2 == 0]))
print(score)
