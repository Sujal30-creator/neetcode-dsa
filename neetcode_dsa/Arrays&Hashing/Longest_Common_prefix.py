class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        hashmap = dict()
        ans = str()
        count = 0

        len_strs = len(strs)

        for i in range(len_strs):
            for char in strs[i]:
                if char in hashmap:
                    hashmap[char]+=1
                else:
                    hashmap[char] = 1


        for key,value in hashmap.items():
            if value == len_strs:
                ans = ans + key
            else:
                break
            
        return ans
            
if __name__=="__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(strs=["dance","dag","danger","damage"]))