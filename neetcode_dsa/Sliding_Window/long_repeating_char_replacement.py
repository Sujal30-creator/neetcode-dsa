class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R=0,1
        count = k
        max_len = 1

        while R<len(s):
            if s[L] != s[R]:
                if count == 0:
                    max_len = max(max_len,R-L)
                    L+=1
                    R=L
                    count = k
                else:
                    count -= 1
            
            R+=1

        return max_len

if __name__== "__main__":
    sol = Solution()
    print(sol.characterReplacement(s="ABAB",k=2))