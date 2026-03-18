class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(char for char in s if char.isalnum())
        cleaned_str = cleaned_str.lower()
        counter = True
        start, end = 0, len(cleaned_str)-1

        while (start<end):
            if cleaned_str[start] == cleaned_str[end]:
                start += 1
                end -= 1
            elif cleaned_str[start] != cleaned_str[end]:
                if counter:
                    counter = False
                    end -= 1
                else:
                    return False
                
        if start == end:
            return
        return True



if __name__=="__main__":
    sol = Solution()
    strs = "abcca"
    print(sol.validPalindrome(strs))
         
    