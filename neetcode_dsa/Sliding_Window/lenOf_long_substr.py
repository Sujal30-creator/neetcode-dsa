class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result, hashmap = 0, 0, 0, dict()
        
        while (right<len(s)):
            if (s[right] in hashmap):
                left = max(hashmap[s[right]]+1,left)
            hashmap[s[right]] = right
            result = max(result, ((right-left)+1))
            right += 1
        return result

        #Optimal Soln. :-
        # mp = {}
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l = max(mp[s[r]] + 1, l)
        #     mp[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s="zxyzxyz"))