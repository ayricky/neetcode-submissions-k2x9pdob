import time

class Twitter:

    def __init__(self):
        self.user_following: dict[str, set] = defaultdict(set)
        self.user_followers: dict[str, set] = defaultdict(set)
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

        
    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        valid_users = self.user_following[userId]

        for user_id, tweet_id in self.tweets[::-1]:
            if user_id == userId or user_id in valid_users:
                news_feed.append(tweet_id)
            if len(news_feed) == 10:
                break
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        self.user_followers[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
        if followerId in self.user_followers[followeeId]:
            self.user_followers[followeeId].remove(followerId)
        
