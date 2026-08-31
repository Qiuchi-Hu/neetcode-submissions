import heapq
class User:
    def __init__(self, userId):
        self.posts = []
        self.follows = set([userId])
    
    def tweet(self, tweetId: int, seq: int):
        self.posts.append((seq, tweetId))
        if len(self.posts) > 10:
            self.posts = self.posts[1:]

    def follow(self, userId: int):
        self.follows.add(userId)

    def unfollow(self, userId: int):
        self.follows.discard(userId)

class Users:
    def __init__(self):
        self.users = {}
        self.seq = 0
    
    def maybe_add_user(self, userId: int):
        if userId not in self.users:
            self.users[userId] = User(userId)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.maybe_add_user(userId)
        self.users[userId].tweet(tweetId, self.seq)
        self.seq -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.maybe_add_user(userId)
        all_posts = []
        for followerId in self.users[userId].follows:
            self.maybe_add_user(followerId)
            all_posts += self.users[followerId].posts

        heapq.heapify(all_posts)
        output = []
        while all_posts and len(output) < 10:
            output.append(heapq.heappop(all_posts)[1])
        return output
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.maybe_add_user(followerId)
        self.users[followerId].follow(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.maybe_add_user(followerId)
        self.users[followerId].unfollow(followeeId)


class Twitter:

    def __init__(self):
        self.users = Users()
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.postTweet(userId, tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        return self.users.getNewsFeed(userId)
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.follow(followerId, followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users.unfollow(followerId, followeeId)
        
