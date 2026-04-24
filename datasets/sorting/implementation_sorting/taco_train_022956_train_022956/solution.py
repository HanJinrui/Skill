for _ in range(eval(input())):
	n = eval(input())
	arr= list(map(int, input().split()))
	klen= eval(input())
	minArr = [0] * n
	currLen = 1
	minArr[0] = arr[0]
	for i in range(1, n):
		if arr[i] < minArr[0]:
			minArr[0] = arr[i]
		elif arr[i] > minArr[currLen-1]:
			if currLen < klen:
				minArr[currLen] = arr[i]
				currLen += 1
		else:
			low = -1
			high= currLen - 1
			while low < high:
				mid = low + (high - low) / 2
				if minArr[mid] < arr[i]:
					low = mid + 1
				else:
					high = mid
			minArr[high] = arr[i]
	if currLen < klen:
		print("-1")
	else:
		print(minArr[klen - 1])
