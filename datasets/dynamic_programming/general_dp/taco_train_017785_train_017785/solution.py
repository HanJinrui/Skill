a = {0:0}
 
def f(b):
	if b in a:
		return a[b]
	else:
		a[b] = max(b, f(b/4)+f(b/3)+f(b/2))
		return a[b]
while True:
	try:
		print(f(int(input())))
	except:
		break
