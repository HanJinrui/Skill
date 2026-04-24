n = int(input())
stones = list(map(lambda t: int(t), input().split()))
q = int(input())
queries = list(map(lambda t: int(t), input().split()))
stones.sort()
added_stones = []
added_stones.append(stones[0])
for i in range(1, n, 1):
	added_stones.append(stones[i] + added_stones[i - 1])
computed_queries = {}
for (qidx, qq) in enumerate(queries):
	if qq in computed_queries:
		queries[qidx] = computed_queries[qq]
		continue
	i = n - 2
	multiplier = 1
	cost = 0
	while i >= 0:
		pp = pow(qq, multiplier)
		nexti = i - pp
		if nexti < 0:
			cost += added_stones[i] * multiplier
			break
		cost += (added_stones[i] - added_stones[nexti]) * multiplier
		multiplier += 1
		i = nexti
	queries[qidx] = cost
	computed_queries[qq] = cost
print(*queries, sep=' ')
