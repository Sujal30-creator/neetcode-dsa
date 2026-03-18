class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ptr1 , ptr2 = 0, 1

        while ptr2<len(nums):
            if nums[ptr1] == nums[ptr2]:
                nums.pop(ptr2)
            else:
                ptr1+=1
                ptr2+=1
        print(nums)
        return len(nums)
    
if __name__=="__main__":
    sol = Solution()
    print(sol.removeDuplicates(nums = [2,10,10,30,30,30]))