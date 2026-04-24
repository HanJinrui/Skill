class Solution:

	def getMaxArea(self, h):
		h.append(0)
		stack = []
		i = 0
		area = -1
		while i < len(h):
			if not stack or h[stack[-1]] < h[i]:
				stack.append(i)
				i += 1
			else:
				top = stack.pop()
				area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
		return area
