class Solution:
     def search(self, nums: list[int], target: int):        
        
        start, end = 0, len(nums)-1

        while start<=end:
            middle = (start+end) // 2

            if (nums[middle]==target):
                return middle
            elif (nums[middle] > target):
                end = middle-1
            elif (nums[middle]<target):
                start = middle+1
        
        return -1
     
if __name__=="__main__":
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target = 8
    print(sol.search(nums=nums,target=target))

