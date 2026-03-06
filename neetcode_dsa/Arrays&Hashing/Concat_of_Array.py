class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans
    
if __name__=="__main__":
    sol = Solution()
    print(sol.getConcatenation(nums=[1,4,1,2]))