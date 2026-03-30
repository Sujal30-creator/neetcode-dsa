class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        ans = list()
        for i in range(len(nums)):
            j = 0
            if not ans:
                ans.append(nums[i])
            else:
                while j<len(ans) and ans[j]<nums[i]:
                    j+=1
                ans.insert(j, nums[i])

        return ans


if __name__=="__main__":
    sol = Solution()
    print(sol.sortArray(nums=[5,10,2,1,3]))