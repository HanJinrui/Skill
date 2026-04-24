from itertools import repeat
M = 200010
adjList = [[] for i in repeat(None, M)]
dppp = [0 for i in range(M)]
dpp1 = [0 for i in range(M)]
myStr = ''
done = [0 for i in range(M)]
maxInd = [0 for i in range(M)]
N = 0

def dfs(node, dad):
	dpp1[node] = maxInd[node]
	for i in range(len(adjList[node])):
		v = adjList[node][i]
		if v != dad:
			dfs(v, node)
			dppp[node] = dppp[node] + max(dppp[v], dpp1[v])
			dpp1[node] = dpp1[node] + dppp[v]
	done[node] = 0
Q = int(input())
for q in range(Q):
	myStr = str(input())
	u = myStr.split(' ')
	if myStr[0] == 'A':
		x = int(u[1])
		N += 1
		maxInd[N] = x
		done[N] = 1
	elif myStr[0] == 'B':
		x = int(u[1])
		y = int(u[2])
		adjList[x].append(y)
		adjList[y].append(x)
	elif myStr[0] == 'C':
		x = int(u[1])
		dfs(x, x)
		N += 1
		maxInd[N] = max(dppp[x], dpp1[x])
		done[N] = 1
ans = 0
for i in range(N):
	if done[i + 1] == 1:
		dfs(i + 1, i + 1)
		ans += max(dppp[i + 1], dpp1[i + 1])
print(str(ans))
