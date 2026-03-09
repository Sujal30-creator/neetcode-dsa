class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left,right = 0,1
        profit = 0

        while right<len(prices):
            if prices[right]>prices[left]:
                profit += prices[right]-prices[left]

            right+=1
            left+=1

        return profit
    
if __name__=="__main__":
    sol = Solution()
    prices = [10,1,5,6,7,1]
    print(sol.maxProfit(prices=prices))
            