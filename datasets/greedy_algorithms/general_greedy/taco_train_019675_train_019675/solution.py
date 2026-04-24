n = int(input())
seq = list(map(int, input().split()))
(soma, melhor) = (0, 0)
for i in seq:
	soma = max(0, soma + i)
	melhor = max(melhor, soma)
print(2 * melhor - sum(seq))
