class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0,0
        new_str = ""

        while ptr1<len(word1) and ptr2<len(word2):
            new_str = new_str + word1[ptr1] + word2[ptr2]
            ptr1+=1
            ptr2+=1
        print(ptr1,ptr2,len(word1)-1)
        if ptr1 == len(word1):
            new_str = new_str + word2[ptr2:]
        elif ptr2 == len(word2):
            new_str = new_str + word1[ptr1:]
        return new_str
    
if __name__=="__main__":
    sol = Solution()
    print(sol.mergeAlternately(word1="ab", word2="abbxxc"))