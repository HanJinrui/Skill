def main():
	t=eval(input())
	while t>0:
		t=t-1
		n=eval(input())
		w=eval(input())
		if 0==n:
			print(0)
			continue
		wi=[int(s) for s in input().split()]
		vi=[int(s) for s in input().split()]
		table = [[0 for ww in range(w)] for cc in range(n+1)]
		for i in range(1,n+1):
			for j in range(1,w+1):
				if wi[i-1]<=j:
					diff=j-wi[i-1]
					add=0
					if diff > 0:
						add=table[i-1][diff-1]
					table[i][j-1] = max(table[i-1][j-1],add+vi[i-1])
				else:
					table[i][j-1] = table[i-1][j-1]
		print(table[n][w-1])

main()
