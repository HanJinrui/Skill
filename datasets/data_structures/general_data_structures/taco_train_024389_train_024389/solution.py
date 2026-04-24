def push_front_pf(dq, x):
	dq.appendleft(x)

def push_back_pb(dq, x):
	dq.append(x)

def front_dq(dq):
	if len(dq) != 0:
		return dq[0]
	else:
		return -1

def pop_back_ppb(dq):
	if dq:
		return dq.pop()
