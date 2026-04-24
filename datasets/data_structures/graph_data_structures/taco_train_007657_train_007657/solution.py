class Solution:

	def ShortestPath(self, S):
		ans = []
		i = 0
		curX = 0
		curY = 0
		while i < len(S):
			nextX = (ord(S[i]) - ord('A')) // 5
			nextY = (ord(S[i]) - ord('B') + 1) % 5
			while curY > nextY:
				ans.append('LEFT')
				curY -= 1
			while curY < nextY:
				ans.append('RIGHT')
				curY += 1
			while curX > nextX:
				ans.append('UP')
				curX -= 1
			while curX < nextX:
				ans.append('DOWN')
				curX += 1
			ans.append('OK')
			i += 1
		return ans
