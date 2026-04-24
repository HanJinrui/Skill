from bisect import insort
T = int(input())
tasks = []
maxt = used_time = 0
for _ in range(T):
	task = [int(x) for x in input().split()]
	if maxt and task[0] <= tasks[0][0]:
		used_time += task[1]
		print(max(0, used_time + tasks[0][1] - tasks[0][0]))
		continue
	insort(tasks, task)
	maxt = idx = 0
	t = used_time
	for (i, (td, tm)) in enumerate(tasks):
		t += tm
		if t - td > maxt:
			idx = i
			maxt = t - td
	if maxt:
		for _ in range(idx):
			used_time += tasks.pop(0)[1]
	print(maxt)
