class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        #slow is at the starting point (0 step)
        #fast is at the 1st step
        #at time t, slow and fast has the relationship of 2t+1 instead of 2t
        slow = 0
        fast = nums[0]


        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            #print("fast: ",fast)
            #print("slow: ", slow)
            #count+=1

        print("send out sec_slow")
        sec_slow = 0
        while slow != sec_slow:
            sec_slow=nums[sec_slow]
            slow = nums[slow]

        return sec_slow
        '''

        slow = nums[0]
        fast = nums[nums[0]]
        #count =0

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            #print("fast: ",fast)
            #print("slow: ", slow)
            #count+=1

        print("send out sec_slow")
        sec_slow = 0
        while slow != sec_slow:
            sec_slow=nums[sec_slow]
            slow = nums[slow]

        return sec_slow