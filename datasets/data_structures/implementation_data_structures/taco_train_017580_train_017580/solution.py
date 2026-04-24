import sys
(n, m) = map(int, input().split(' '))
inp = []
guess = [0] * (n + 1)
for i in range(n):
	temp = int(input())
	inp.append(temp)
	if temp < 0:
		m -= 1
		guess[-temp] -= 1
	else:
		guess[temp] += 1
dic = {temp for temp in range(1, n + 1) if guess[temp] == m}
if len(dic) == 0:
	for i in range(n):
		print('Not defined')
elif len(dic) == 1:
	temp = dic.pop()
	for i in inp:
		if i == temp or (i < 0 and i + temp):
			print('Truth')
		else:
			print('Lie')
else:
	temp = dic.update({-i for i in dic})
	for i in inp:
		if i in dic:
			print('Not defined')
		elif i < 0:
			print('Truth')
		else:
			print('Lie')
