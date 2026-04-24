def time_split(time):
	d = {}
	hh = int(time[0])
	mm = int(time[1])
	ss = int(time[2])
	d["h1"] = hh/10
	d["h2"] = hh%10
	d["m1"] = mm/10
	d["m2"] = mm%10
	d["s1"] = ss/10
	d["s2"] = ss%10
	
	return d

def inc_clock(d):
	hh = d["h1"]*10 + d["h2"]
	mm = d["m1"]*10 + d["m2"]
	ss = d["s1"]*10 + d["s2"]
	
	if ss < 59:
		ss += 1
	else:
		ss = 0
		if mm < 59:
			mm += 1
		else:
			mm = 0
			if hh < 23:
				hh += 1
			else:
				hh = 0

	dict = time_split([hh,mm,ss])
	return dict

 
def get_input():
	tc = int(input())
	timing_list = []
	for i in range(0,tc):
		timing_list.append(input())
		
	for j in range(0,len(timing_list)):

		s = set()
		d = {}
		time = timing_list[j]
		time = time.split(":")
		d = time_split(time)
		
		while True:
			s.update(list(d.values()))
			if len(s) == 6:
				break
			
			else:
				d = inc_clock(d)
				s.clear()
				s.update(list(d.values()))

		print("%d%d%s%d%d%s%d%d" % (d["h1"],d["h2"],":",d["m1"],d["m2"],":",d["s1"],d["s2"]))


get_input()
