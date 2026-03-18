class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1, ptr2 = 0, len(s)-1
        dummy = str()

        while ptr1<ptr2:
            dummy = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = dummy
            ptr1+=1
            ptr2-=1

        return s

if __name__=="__main__":
    sol = Solution()
    print(sol.reverseString(s=["n","e","e","t"])) 

