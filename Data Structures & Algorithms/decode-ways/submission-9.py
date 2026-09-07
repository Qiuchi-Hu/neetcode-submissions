class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        s2 = "0"+s
        s2_len = len(s2)
        if s2_len == 2:
            return 1

        count = [0] * s2_len
        count[1] = 1

        for i in range(2,s2_len):
            prev = int(s2[i-1])
            cur = int(s2[i])
            if not prev and not cur:
                return 0

            if cur != 0:
                count[i] += count[i-1]

            if 10 <= prev * 10 + cur <= 26:
                count[i] += max(count[i-2],1)

        
        print(count)
        return count[-1]
            