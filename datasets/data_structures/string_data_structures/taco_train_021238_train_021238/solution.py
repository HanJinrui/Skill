class Twitter:

	def __init__(self):
		self.dp = []
		self.f_data = dict()

	def postTweet(self, userId: int, tweetId: int):
		self.dp.append([userId, tweetId])

	def getNewsFeed(self, userId: int):
		if self.f_data.get(userId) == None:
			self.f_data[userId] = []
		return [x[1] for x in self.dp if x[0] in [userId, *self.f_data[userId]]][-10:][::-1]

	def follow(self, followerId: int, followeeId: int):
		if self.f_data.get(followerId) == None:
			self.f_data[followerId] = []
		self.f_data[followerId].append(followeeId)

	def unfollow(self, followerId: int, followeeId: int):
		self.f_data[followerId].remove(followeeId)
