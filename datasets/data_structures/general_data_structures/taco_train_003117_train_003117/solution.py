a = []
maxa = 0
mina = 100001
for _ in range(int(input())):
	b = input().split()
	if b[0] == "1":
		x = int(b[1])
		a.append(x)
		maxa = max(maxa, x)
		mina = min(mina, x)
	elif b[0] == "2":
		x = int(b[1])
		if x in a:
			a.remove(x)
			if len(a):
				if x == maxa:
					maxa = max(a)
				elif x == mina:
					mina = min(a)
			else:
				maxa = 0
				mina = 100001
		else:
			print(-1)
	elif b[0] == "3":
		print(maxa if len(a) else -1)
	else:
		print(mina if len(a) else -1)
