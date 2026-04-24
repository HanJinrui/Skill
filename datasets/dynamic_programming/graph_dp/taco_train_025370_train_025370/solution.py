def dist(pos1: list, pos2: list) -> int:
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def list2bin(n: int, lst: list) -> str:
	num = 0
	for x in lst:
		num += 1 << x
	return f'{num:08b}'

def pos2str(pos: list) -> str:
	return '--'.join(map(str, pos))

def min_chef(chefs: list, tools: list, htools: list, rem_tools: list, pos: list, cost: int, dp: dict) -> tuple:
	hkey = list2bin(len(tools), htools)
	rkey = list2bin(len(tools), rem_tools)
	pkey = pos2str(pos)
	for (i, ti) in enumerate(htools):
		c = chefs[ti]
		dc = dist(pos, c)
		nhtools = htools[:i] + htools[i + 1:]
		hkey = list2bin(len(tools), nhtools)
		rkey = list2bin(len(tools), rem_tools)
		pkey = pos2str(c)
		if not dp.get(hkey, {}).get(rkey, {}).get(pkey):
			dp = recurse(chefs, tools, nhtools, rem_tools, c, dp)
		cost = min(cost, dc + dp[hkey][rkey][pkey])
	return (cost, dp)

def min_tool(chefs: list, tools: list, htools: list, rem_tools: list, pos: list, cost: int, dp: dict) -> tuple:
	for (i, ti) in enumerate(rem_tools):
		t = tools[ti]
		dt = dist(pos, t)
		nhtools = htools + [ti]
		nrem_tools = rem_tools[:i] + rem_tools[i + 1:]
		hkey = list2bin(len(tools), nhtools)
		rkey = list2bin(len(tools), nrem_tools)
		pkey = pos2str(t)
		if not dp.get(hkey, {}).get(rkey, {}).get(pkey):
			dp = recurse(chefs, tools, nhtools, nrem_tools, t, dp)
		cost = min(cost, dt + dp[hkey][rkey][pkey])
	return (cost, dp)

def recurse(chefs: list, tools: list, htools: list, rem_tools: list, pos: list, dp: dict) -> dict:
	hkey = list2bin(len(tools), htools)
	rkey = list2bin(len(tools), rem_tools)
	pkey = pos2str(pos)
	if hkey not in dp:
		dp[hkey] = {}
	if rkey not in dp[hkey]:
		dp[hkey][rkey] = {}
	if pkey not in dp[hkey][rkey]:
		if len(htools) > 2:
			cost = 1000000000.0
		elif len(htools) == 0 and len(rem_tools) == 0:
			cost = abs(pos[0]) + abs(pos[1])
		else:
			(cost, dp) = min_chef(chefs, tools, htools, rem_tools, pos, 1000000000.0, dp)
			(cost, dp) = min_tool(chefs, tools, htools, rem_tools, pos, cost, dp)
		dp[hkey][rkey][pkey] = cost
	return dp

def solve(chefs: list, tools: list, n: int) -> int:
	rem_tools = list(range(n))
	dp = recurse(chefs, tools, [], rem_tools, [0, 0], {})
	hkey = list2bin(n, [])
	rkey = list2bin(n, rem_tools)
	pkey = pos2str([0, 0])
	return dp[hkey][rkey][pkey]

def main():
	t = int(input().strip())
	for _ in range(t):
		n = int(input().strip())
		(chefs, tools) = ([], [])
		for i in range(n):
			(cx, cy, tx, ty) = map(int, input().strip().split())
			chefs.append([cx, cy])
			tools.append([tx, ty])
		print(solve(chefs, tools, n))
main()
