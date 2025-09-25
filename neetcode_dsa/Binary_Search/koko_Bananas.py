import math

class Solution:
     def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start, end = 1, max(piles)
        ans = end
        while (start<=end):
            middle = (start+end) // 2
            total_hours=0
            
            
            for pile in piles:
                total_hours += math.ceil(pile / middle)
            
            if (h < total_hours):
                start = middle+1
            else:
                ans = middle
                end = middle-1
        
        return ans
     
if __name__=="__main__":
    sol = Solution()
    nums = [3,6,7,11]
    target = 8
    print(sol.minEatingSpeed(piles=nums,h=target))