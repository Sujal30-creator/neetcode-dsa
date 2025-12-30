class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #O(26.n)
        # l = r = res = 0
        # hashmap = dict()

        # for r in range(len(s)):
        #     if s[r] in hashmap:
        #         hashmap[s[r]] += 1
        #     else:
        #         hashmap[s[r]] = 1

        #     window_len = (r-l)+1
        #     most_freq = max(hashmap.values())
        #     count = window_len - most_freq

        #     if count <= k:
        #         res = max(res,window_len)
        #     else:
        #         hashmap[s[l]] -= 1
        #         l+=1         
        # return res

        #O(n)
        l = r = res = 0
        hashmap = dict()
        max_f = 1

        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
                max_f = max(max_f,hashmap[s[r]])
            else:
                hashmap[s[r]] = 1

            window_len = (r-l)+1
            count = window_len - max_f

            if count <= k:
                res = max(res,window_len)
            else:
                hashmap[s[l]] -= 1
                l+=1       
        return res

if __name__== "__main__":
    sol = Solution()
    print(sol.characterReplacement(s="AABABBA",k=1))