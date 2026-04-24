class Solution:

	def MissingNo(self, M):
		import numpy as np
		M = np.array(M)
		SR = M.sum(axis=0)
		SC = M.sum(axis=1)
		(zr, zc, X) = (np.argmin(SR), np.argmin(SC), SR.max())
		add = X - SR[zr]
		(SR[zr], SC[zc], M[zr, zc]) = (SR[zr] + add, SC[zc] + add, M[zr, zc] + add)
		if add <= 0:
			return -1
		if not np.array_equal(SR, SC):
			return -1
		if M.diagonal().sum() != X:
			return -1
		if np.fliplr(M).diagonal().sum() != X:
			return -1
		return add
