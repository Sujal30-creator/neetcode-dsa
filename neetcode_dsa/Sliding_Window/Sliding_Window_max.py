import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # L, R = 0, k
        # ans = list()

        # while R<=len(nums):
        #     ans.append(max(nums[L:R]))
        #     L+=1
        #     R+=1

        # return ans
    
        ans = []
        window = collections.deque()
        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            
            window.append(right)

            if window[0] <= right - k:
                window.popleft()

            if right >= k - 1:
                ans.append(nums[window[0]])

        return ans

if __name__=="__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums=[1,2,1,0,4,2,6], k=3))