mem={}
def sum_digits3(n):
	n=n**2
	r = 0
	while n:
		 r, n = r + n % 10, n // 10
	return r

def findnature(n):
	 if(n in mem):return mem[n]
	 if(n==1 or n==4): return 1
	 if(n==9 or n==13): return -1
	 ans=findnature(sum_digits3(n))
	 mem[n]=ans
	 return ans

for t in range(int(input())):
	 if(findnature(int(input()))==1):print("YES")
	 else:print('NO')
