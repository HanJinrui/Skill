import sys

N=int(eval(input()))
res = []

def check(nums):
	nums1 = set()
	nums1.add(0)
	for i in nums:
		nums2 = nums1.copy()
		for j in nums1:
			nums2.add(i+j)
		nums1 = nums2.copy()
	return len(nums1)

for i in range(N):
	tot = int(input())
	nums = [int(i) for i in str(input()).split(' ')]
	res.append(check(nums))

for x in res:
	print(x)
