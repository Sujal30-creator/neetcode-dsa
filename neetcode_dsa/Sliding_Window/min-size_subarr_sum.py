class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # left, right = 0,1 
        # res = 0
        # count = 0

        # while right < len(nums)+1:
        #     res = sum(nums[left:right])
        #     if res >= target:
        #         if count == 0:
        #             count = len(nums)
        #         count = min(count,right-left)
        #         left += 1
        #         right = left
        #     right += 1
        # return count

        left = 0
        max_length = len(nums)
        flag = False
        sum = 0
        
        for right in range(len(nums)):
            while sum + nums[right] >= target:
                max_length = min(max_length, right - left + 1)
                sum -= nums[left]
                left += 1
                flag = True

            sum += nums[right]
        
        return max_length if flag == True else 0



if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(target=4, nums=[1,1,1])) 