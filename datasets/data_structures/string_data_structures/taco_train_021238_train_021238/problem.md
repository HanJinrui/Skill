Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
	postTweet (userId, tweetId): Compose a new tweet.
	getNewsFeed (userId): Retrieve the 10 most recent tweet ids in the user's news feed (If total number of tweets in news feed is less than 10, then return all). Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
	follow (followerId, followeeId): Follower follows a followee.
	unfollow (followerId, followeeId): Follower unfollows a followee.
Example 1:
Input:
postTweet(1, 5);
getNewsFeed(1);
follow(1, 2);
postTweet(2, 6);
getNewsFeed(1);
unfollow(1, 2);
getNewsFeed(1);
Output:
[5]
[6, 5]
[5]
Explanation: 
postTweet(1,5): User 1 posts a new tweet (id=5)
getNewsFeed(1): Return a list with 1 tweet [5]
follow(1,2)   : User 1 follows user 2.
postTweet(2,6): User 2 posts a new tweet (id=6)
getNewsFeed(1): Return a list with 2 tweets 
[6,5]. One his own tweet and one followee's tweet
(sorted from most recent to least recent).
unfollow(1,2) : User 1 unfollows user 2
getNewsFeed(1): Return a list with 1 tweet [5],
because user 1 is no longer following anyone.
Example 2:
Input:
follow(1, 2);
postTweet(1, 3);
getNewsFeed(2);
Output:
[]
Explanation:
follow(1,2)   : User 1 follows user 2.
postTweet(1,3): User 1 posts a new tweet (id=3)
getNewsFeed(2): Return a list with 0 tweet [],
because user2 have no tweets and don't follow
anyone (user1 follows user 2 but user 2 don't
follow anyone)
Your Task:  
You don't need to read input or print anything. Your task is to design your data structure inside the class Twitter and complete the functions postTweet(), getNewsFeed(), follow(), unfollow(), and the constructor.
Constraints:
1 <= no. of queries <= 1000
1 <= userId, tweetId, followerId, followeeId <= 10^{5}

Starter code:
```python
#User function Template for python3



class Twitter:

    # Compose a new tweet

    def postTweet(self, userId: int, tweetId: int):

        # Code here

        

    # Retrieve the 10 most recent tweet ids as mentioned in question

    def getNewsFeed(self, userId: int):

        # Code here

        

    # Follower follows a followee. If the operation is invalid, it should be a no-op.

    def follow(self, followerId: int, followeeId: int):

        # Code here

        

    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.

    def unfollow(self, followerId: int, followeeId: int):

        # Code here
```
