from sys import stdin
data = {}
counts = {}
for line in stdin:
	a = line[3:].split('\\')
	a[0] = line[0] + a[0]
	counts[a[0]] = counts.get(a[0], 0) + 1
	if a[0] not in data:
		data[a[0]] = set()
	acc = '/'
	for f in a[1:-1]:
		acc += f
		data[a[0]].add(acc)
		acc += '/'
print(max([len(data[k]) for k in data]), max([counts[k] for k in counts]))
