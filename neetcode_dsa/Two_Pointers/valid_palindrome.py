class Solution(object):
    def isPalindrome(self, s):
        cleaned_str = "".join(char for char in s if char.isalnum())
        cleaned_str = cleaned_str.lower()

        start, end = 0, len(cleaned_str)-1
        
        while (start < end):
            if (cleaned_str[start] != cleaned_str[end]):
                return False
            
            start += 1
            end -= 1
        return True         

if __name__=="__main__":
    sol = Solution()
    strs = "Was it a car or a cat M saw?"
    print(sol.isPalindrome(strs))
        