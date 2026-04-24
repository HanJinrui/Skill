paths=0
def route(i,j):
	if i==n-1 and j==n-1:
		global paths
		paths+=1
		return 0
	
	mark[i][j]=1
	if ((j+1)<=n-1 and mark[i][j+1]==0 and mat[i][j+1]==0):
		route(i,j+1)
		
	if ((j-1)>=0 and mark[i][j-1]==0 and mat[i][j-1]==0):
		route(i,j-1)
	
	if ((i+1)<=n-1 and mark[i+1][j]==0 and mat[i+1][j]==0):
		route(i+1,j)
	
	if ((i-1)>=0 and mark[i-1][j]==0 and mat[i-1][j]==0):
		route(i-1,j)
	mark[i][j] = 0
	return 0


t = eval(input())
while(t>0):
	mat = []
	mark = []
	global paths
	paths = 0
	x = eval(input())
	for _ in range(x):
		l = list(map(int, input().split()))
		mat.append(l)
		a = [0]*len(l)
		mark.append(a)
	n = len(mat)

	route(0,0)
	print(paths)
	t-=1
