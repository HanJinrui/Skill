import itertools
import collections
s1 = input()
s2 = input()
rules = collections.defaultdict(set)
n = int(input())
for i in range(n):
	rule = input()
	target = rule[-2:]
	source = rule[0]
	rules[target].add(source)

def substrings_of_precise_length(s, l):
	for start_pos in range(len(s) - l + 1):
		yield s[start_pos:start_pos + l]

def substrings_of_minimum_length(s, minlen):
	return itertools.chain.from_iterable((substrings_of_precise_length(s, l) for l in range(minlen, len(s) + 1)))

def partitions_of_string(s):
	for l1 in range(1, len(s)):
		yield (s[:l1], s[l1:])
ancestors = collections.defaultdict(set)

def update_ancestors(ancestors, rules, s):
	for c in s:
		ancestors[c].add(c)
	for sub in substrings_of_minimum_length(s, 2):
		for (sub1, sub2) in partitions_of_string(sub):
			for (target, sources) in rules.items():
				if target[0] in ancestors[sub1] and target[1] in ancestors[sub2]:
					ancestors[sub].update(sources)
update_ancestors(ancestors, rules, s1)
update_ancestors(ancestors, rules, s2)

def prefixes(s):
	for l in range(1, len(s) + 1):
		yield s[:l]

def determine_shortest_common_ancestor(ancestors, s1, s2):
	shortest_common_ancestor = collections.defaultdict(lambda : float('inf'))
	for (pre1, pre2) in itertools.product(prefixes(s1), prefixes(s2)):
		if not ancestors[pre1].isdisjoint(ancestors[pre2]):
			shortest_common_ancestor[pre1, pre2] = 1
		temp = shortest_common_ancestor[pre1, pre2]
		for ((sub1a, sub1b), (sub2a, sub2b)) in itertools.product(partitions_of_string(pre1), partitions_of_string(pre2)):
			if not ancestors[sub1b].isdisjoint(ancestors[sub2b]):
				temp = min(temp, shortest_common_ancestor[sub1a, sub2a] + 1)
		shortest_common_ancestor[pre1, pre2] = temp
	return shortest_common_ancestor[s1, s2]
answer = determine_shortest_common_ancestor(ancestors, s1, s2)
if answer == float('inf'):
	print(-1)
else:
	print(answer)
