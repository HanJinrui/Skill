from bisect import bisect
max_p = 10
N = int(input())
lst = []
for _ in range(N):
	lst.append(input())
ans = {}
for p_size in range(max_p + 1):
	for i in range(len(lst)):
		s = lst[i]
		cur_p = s[:p_size]
		if cur_p in ans:
			p_lst = ans[cur_p]
			last_str = lst[p_lst[len(p_lst) - 1]]
			if s < last_str:
				p_lst.append(i)
		else:
			ans[cur_p] = [i]
Q = int(input())
for _ in range(Q):
	(R, P) = input().split()
	R = int(R) - 1
	while True:
		if P in ans:
			cur_lst = ans[P]
			res = bisect(cur_lst, R)
			if res - 1 >= 0:
				print(lst[cur_lst[res - 1]])
				break
		P = P[:-1]
