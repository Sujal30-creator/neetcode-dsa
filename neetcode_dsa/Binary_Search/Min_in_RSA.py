class Solution:
     def findMin(self, nums: list[int]) -> int:        
        start, end = 0, len(nums)-1

        if (nums[start]<=nums[end]):
            return nums[0]
        else:
            while (start<end):
                middle = (start+end) // 2

                if nums[middle] > nums[end]:
                    start = middle+1
                else:
                    end = middle

            return nums[start]
     
if __name__=="__main__":
    sol = Solution()
    nums = [6,1,2,3,4,5]
    print(sol.findMin(nums=nums))

