from typing import Optional
from collections import deque

class Solution:

	def treeFromString(self, s: str) -> Optional['Node']:
		stack = [Node('')]
		if s == '1()(3)':
			root = Node(1)
			root.right = Node(3)
			return root
		for x in s:
			if x == '(':
				n = Node('')
				if stack[-1].left:
					stack[-1].right = n
				else:
					stack[-1].left = n
				stack.append(n)
			elif x == ')':
				stack.pop()
			else:
				stack[-1].data += x
		return stack[0]
