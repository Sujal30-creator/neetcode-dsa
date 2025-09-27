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
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s="zxyzxyz"))