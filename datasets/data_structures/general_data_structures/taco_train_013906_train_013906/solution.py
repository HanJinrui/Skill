def circularSubarraySum(arr, n):
	cs = mxs = mns = mx = mn = arr[0]
	for i in range(1, n):
		mx = max(arr[i], mx + arr[i])
		mxs = max(mxs, mx)
		mn = min(arr[i], mn + arr[i])
		mns = min(mns, mn)
		cs += arr[i]
	if mxs > 0:
		return max(mxs, cs - mns)
	else:
		return mxs
