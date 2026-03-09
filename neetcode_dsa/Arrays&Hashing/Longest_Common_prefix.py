class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for char1,char2 in zip(strs[0],strs[1]):
            if char1 == char2:
                prefix += char1
            else:
                break

        print(len(prefix))

        if len(prefix)>0:
            for i in range(2,len(strs)):
                if strs[i][0:len(prefix)] == prefix:
                    continue
                else:
                    return ""

        return prefix

if __name__=="__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(strs=["dance","dag","danger","damage"]))