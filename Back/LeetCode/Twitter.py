from typing import List

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followList = dict()
        self.twitter = list()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.twitter.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result = list()
        followeeIdList = list()
        if userId in self.followList.keys():
            followeeIdList = list(self.followList[userId])

        for user, tweet in self.twitter[::-1]:
            if userId == user:
                result.append(tweet)
            else:
                if user in followeeIdList:
                    result.append(tweet)

            if len(result) >= 10:
                break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followList.keys():
            value = self.followList[followerId]
            value.add(followeeId)
        else:
            self.followList.setdefault(followerId, {followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followList.keys():
            value = self.followList[followerId]
            try:
                value.remove(followeeId)
            except KeyError:
                pass

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)