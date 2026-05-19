class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map: dict[str, set] = defaultdict(set)
        self.tweet_map = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        self.follow_map[userId].add(userId)
        min_heap = []

        for followee in self.follow_map[userId]:
            if followee in self.tweet_map:
                index = len(self.tweet_map[followee]) - 1
                count, tweet_id = self.tweet_map[followee][index]
                heapq.heappush(min_heap, (count, tweet_id, followee, index - 1))
        
        while min_heap and len(news_feed) < 10:
            count, tweet_id, followee, index = heapq.heappop(min_heap)
            news_feed.append(tweet_id)

            if index >= 0:
                count, tweet_id = self.tweet_map[followee][index]
                heapq.heappush(min_heap, (count, tweet_id, followee, index - 1))

        return news_feed



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
