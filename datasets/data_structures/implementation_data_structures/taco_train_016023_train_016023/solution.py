for _ in range(int(input())):
	n,q = list(map(int,input().split()))
	l = []
	t = [0]*n
	for i in range(n):
		l.append(input())
	for i in range(q):
		spender = input()
		amt = int(input())
		p = int(input())
		share = amt/(p+1)
		t[l.index(spender)] += p * share
		for o in range(p):
			#ppl = raw_input()
			t[l.index(input())] -= share
	for i in range(len(t)):
		if t[i]==0:
			print(l[i] + " neither owes nor is owed")
		elif t[i]<0:
			print(l[i] + " owes " + str(abs(t[i])))
		else:
			print(l[i] + " is owed " + str(t[i]))
