class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
            
            if t[j] in hashmap:
                hashmap[t[j]] -= 1
            else:
                return False
        
        keys = hashmap.keys()
        for k in keys:
            if hashmap[k] != 0:
                return False

        return True
    
if __name__=='__main__':
    sol = Solution()
    s= "anagram"
    t= "nagaram"
    print(sol.isAnagram(s, t))