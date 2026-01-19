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


        # Phase 1: The Hare & Tortoise Race
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("slow:" + str(slow))
            print("fast:" + str(fast))
            if slow == fast:
                break

        # Phase 2: Find the cycle entrance (The duplicate)
        slow2 = nums[0]
        print("")
        print("---Phase 2 starts---")
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            print("slow:" + str(slow))
            print("slow2:" + str(slow2))

        return slow

if __name__=="__main__":
    sol = Solution()
    print(sol.findDuplicate(nums = [1,2,3,2,2]))