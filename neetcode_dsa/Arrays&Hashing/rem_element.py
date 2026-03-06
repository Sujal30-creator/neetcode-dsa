class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement(nums = [3,2,2,3], val = 3))
        