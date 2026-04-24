primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
arr=[0]*100000

def gcd(a,b):
	if a%b==0:
		return b
	else:
		return gcd(b,a%b)

def to_sec(h,m,s):
	return (h*60*60) + (m*60) + s
def check_div(h,m,s):
	for e in primes:
		if h%e==0 and m%e==0 and s%e==0:
			return False
	return True

for h in range(24):
	for m in range(60):
		for s in range(60):
			if check_div(h,m,s):
				arr[to_sec(h,m,s)]+=1

for i in range(len(arr)-2,-1,-1):
	arr[i]+=arr[i+1]
	
t=int(input())
for i in range(t):
	h,m,s=(int(e) for e in input().split())
	sec=to_sec(h,m,s)
	good=arr[sec]
	bad=(24*60*60)-sec-good
	temp=gcd(bad,good) if bad!=0 else 1
	print("%d:%d"%(bad/temp,good/temp))
