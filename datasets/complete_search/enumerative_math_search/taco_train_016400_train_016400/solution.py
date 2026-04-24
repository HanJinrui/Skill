def combinacoes(x):
	if x == 1:
		return [[0]]
	else:
		aux = combinacoes(x - 1)
	pilha = []
	par = 0
	for element in aux:
		lmt = max(element) + 1
		if par == 0:
			for j in range(lmt + 1):
				pilha.append(element + [j])
		else:
			for j in range(lmt + 1)[::-1]:
				pilha.append(element + [j])
		par = par ^ 1
	return pilha
n = int(input())
possibilidades = combinacoes(n)
print(len(possibilidades))
for item in possibilidades:
	arranjos = ''
	limit = max(item) + 1
	for group in range(limit):
		arranjos += '{'
		toys = ''
		for i in range(n):
			if item[i] == group:
				toys += '{0},'.format(i + 1)
		arranjos += toys[:-1]
		arranjos += '},'
	print(arranjos[:-1])
