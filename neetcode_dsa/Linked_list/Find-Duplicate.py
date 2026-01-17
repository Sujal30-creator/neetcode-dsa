class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # O(N) Time and space Complexity
        # arr = [0] * len(nums)

        # for n in nums:
        #     if arr[n]:
        #         return n
        #     else:
        #         arr[n] = 1
            
        # return -1


        '''Optimal Soln. with O(N) & O(1) Time and space complexity repectively.'''

        slow = nums[0]
        fast = nums[0]

        for i in range(len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                return nums[slow]
            
        return -1
    


if __name__=="__main__":
    sol = Solution()
    print(sol.findDuplicate(nums = [1,2,3,2,2]))