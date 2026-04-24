from collections import Counter
t= int(input())
if t>=1 and t<=1000:
	for i in range (t):
		a=[]
		n = int(input())
		if n <= 1000000:
			for j in range(n):
				q= int(input())
				a.append(q)
		data = Counter(a)
		print(data.most_common(1)[0][1])
