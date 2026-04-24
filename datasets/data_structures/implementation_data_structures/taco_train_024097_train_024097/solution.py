try:
	data = []
	for _ in range(eval(input())):
		data.append(input())
	best = max(max(len(s) for s in day.replace('S', ' ').replace('E', ' ').split()) for day in data)
	all_data = ''.join(x for day in data for x in day)
	opt = max(len(s) for s in all_data.replace('S', ' ').replace('E', ' ').split())
	print('%s %s' % (best, opt))
except:
	print('0 0')
