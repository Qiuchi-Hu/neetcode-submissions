class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i,string in enumerate(strs):
            char_freq = [0]*26
            for char in string:
                #print("add 1")
                char_freq[ord(char) - ord('a')]+=1
            key = tuple(char_freq)
            #print("key:",key)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        
        output = []
        for key in hashmap:
            print(hashmap[key])
            output.append(hashmap[key])
        
        return output

        