import copy
teams = {}
times = {}

def put_team(s):
	if not s[0] in teams:
		teams[s[0]] = [0, 0, 0, s[0]]
	if not s[1] in teams:
		teams[s[1]] = [0, 0, 0, s[1]]
	(g1, g2) = map(int, s[2].split(':'))
	teams[s[0]][1] -= g1 - g2
	teams[s[1]][1] -= g2 - g1
	teams[s[0]][2] -= g1
	teams[s[1]][2] -= g2
	if g1 > g2:
		teams[s[0]][0] -= 3
	elif g1 < g2:
		teams[s[1]][0] -= 3
	else:
		teams[s[0]][0] -= 1
		teams[s[1]][0] -= 1

def add_times(s):
	times[s[0]] = times.get(s[0], 0) + 1
	times[s[1]] = times.get(s[1], 0) + 1
for _ in range(5):
	s = input().split()
	put_team(s)
	add_times(s)
(t1, t2) = ('BERLAND', '')
for (k, v) in times.items():
	if v == 2 and k != t1:
		t2 = k
cpy_teams = copy.deepcopy(teams)
res = (2000000000.0, 0, 'IMPOSSIBLE')
for g1 in range(60):
	for g2 in range(60):
		if g1 > g2:
			teams = copy.deepcopy(cpy_teams)
			put_team(('%s %s %d:%d' % (t1, t2, g1, g2)).split())
			s = sorted(teams.values())
			if t1 == s[0][3] or t1 == s[1][3]:
				res = min(res, (g1 - g2, g2, '%d:%d' % (g1, g2)))
print(res[-1])
