BLOCK_SIZE = 316

class Query:

	def __init__(self, left, right, number):
		self.left = left
		self.right = right
		self.number = number

	def __lt__(self, other):
		return self.right < other.right
cnt = [0] * (1 << 20)
result = 0
favourite = 0

def add(v):
	global result
	result += cnt[v ^ favourite]
	cnt[v] += 1

def delv(v):
	global result
	cnt[v] -= 1
	result -= cnt[v ^ favourite]
(n, m, favourite) = map(int, input().split())
a = list(map(int, input().split()))
pref = [0] * (n + 1)
for i in range(1, n + 1):
	pref[i] = pref[i - 1] ^ a[i - 1]
blocks = [[] for i in range(n // BLOCK_SIZE + 2)]
for i in range(m):
	(left, right) = map(int, input().split())
	left -= 1
	right += 1
	blocks[left // BLOCK_SIZE].append(Query(left, right, i))
for b in blocks:
	b.sort()
answer = [0] * m
for i in range(len(blocks)):
	left = i * BLOCK_SIZE
	right = left
	for q in blocks[i]:
		while right < q.right:
			add(pref[right])
			right += 1
		while left < q.left:
			delv(pref[left])
			left += 1
		while left > q.left:
			left -= 1
			add(pref[left])
		answer[q.number] = result
	for j in range(left, right):
		delv(pref[j])
print(*answer, sep='\n')
