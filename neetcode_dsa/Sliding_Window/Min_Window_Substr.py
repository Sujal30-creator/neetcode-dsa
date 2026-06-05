class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = dict()
        for i in range(len(s)):
            if s[i] in t:
                if s[i] in hashmap:
                    hashmap[s[i]].append(i)
                else:
                    hashmap[s[i]] = [i]

        print(hashmap)

if __name__=="__main__":
    sol = Solution()
    print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))