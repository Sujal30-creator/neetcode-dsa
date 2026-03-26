class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if len(weights) >= days:
            return days
        


        pass

if __name__=="__main__":
    sol = Solution()
    print(sol.shipWithinDays(weights=[1,2,3,4,5,6,7,8,9,10], days=5))