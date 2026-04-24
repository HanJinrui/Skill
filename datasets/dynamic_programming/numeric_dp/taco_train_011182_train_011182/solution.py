n, k = list(map(int, input().split()))
mat= []
def is_perfect_cube(x):
	x = abs(x)
	return int(round(x ** (1. / 3))) ** 3 == x
for i in range(n):
	l = list(map(int, input().split()))
	sum = 0
	prev = l[0]
	for x in l[0:k]:
		sum += x
	l[0]=sum
	for j in range(1, n-k+1):
		sum = sum-prev + l[j+k-1]
		prev = l[j]
		l[j]=sum
	mat.append(l)
count=0
#print mat
for i in range(n-k+1):
	c = 0
	for z in range(0, k):
		c+=mat[z][i]
		if is_perfect_cube(c):
			count+=1
	for j in range(1, n-k+1):
		c = c - mat[j-1][i]+mat[j+k-1][i]
		if is_perfect_cube(c):
			count+=1
print(count)
