import sys

def ask(x):
	print('? %d' % x)
	sys.stdout.flush()
	x = int(input())
	return x
n = int(input())
t = n // 2
if t & 1:
	print('! -1')
	sys.stdout.flush()
	sys.exit()
l = 1
r = n
while l < r:
	mid = l + r >> 1
	if ask(mid) >= ask((mid + t - 1) % n + 1):
		r = mid
	else:
		l = mid + 1
print('! %d' % l)
sys.stdout.flush()
