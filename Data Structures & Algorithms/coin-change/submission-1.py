class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [-1]*(amount+1)
        len_min_coin = len(min_coin)

        min_coin[0] = 0
        coins.sort(reverse=True)
        for i in range(len_min_coin):
            if min_coin[i] != -1:
                for c in coins:
                    if i+c<len_min_coin:
                        if min_coin[i+c]==-1:
                            min_coin[i+c] = min_coin[i]+1
                        else:
                            min_coin[i+c] = min(min_coin[i]+1,min_coin[i+c])
        
        return min_coin[-1]
