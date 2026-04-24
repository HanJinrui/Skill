class Solution:

	def getMaxandMinProduct(self, arr, n):
		curx = arr[0]
		curin = arr[0]
		minn = arr[0]
		maxx = arr[0]
		i = 1
		while i < n:
			if curx < 1:
				curx = 1
			if curin > -1:
				curin = 1
			curx *= arr[i]
			curin *= arr[i]
			maxx = max(maxx, max(curx, curin))
			minn = min(minn, min(curx, curin))
			curx = max(curx, max(curin, maxx))
			curin = min(curin, min(curx, minn))
			i += 1
		return [minn, maxx]
