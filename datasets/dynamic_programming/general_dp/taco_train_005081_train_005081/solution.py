def wordBreak(s, wordDict):
	if not s:
		return True
	for i in range(1, len(s) + 1):
		if s[:i] in wordDict and wordBreak(s[i:], wordDict):
			return True
	return False
