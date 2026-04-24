from queue import deque

class Solution:

	def wordLadderLength(self, startWord, targetWord, wordList):
		wset = set(wordList)
		q = deque()
		q.append((startWord, 1))
		while q:
			(wrd, steps) = q.popleft()
			if wrd == targetWord:
				return steps
			for j in range(len(wrd)):
				for i in range(26):
					l = list(wrd)
					l[j] = chr(i + 97)
					nwrd = ''.join(l)
					if nwrd in wset:
						q.append((nwrd, steps + 1))
						wset.remove(nwrd)
		return 0
