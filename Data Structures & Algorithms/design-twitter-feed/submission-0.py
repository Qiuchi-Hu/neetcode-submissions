class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = {}
        self.tweetMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count,len(self.tweetMap[userId]),tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = [userId]
        if userId in self.followMap:
            followees.extend(list(self.followMap[userId]))
        
        recent_tweets = []
        for followee in followees:
            if followee in self.tweetMap:
                recent_tweets.extend(self.tweetMap[followee])
        
        heapq.heapify_max(recent_tweets)
        feed = []
        pop_times = min(10,len(recent_tweets))
        for _ in range(pop_times):
            _,_,tweetId = heapq.heappop_max(recent_tweets)
            feed.append(tweetId)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followMap:
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
