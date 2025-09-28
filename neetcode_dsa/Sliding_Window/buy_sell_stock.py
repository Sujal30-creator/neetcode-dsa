class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r =0, 1
        res = 0

        while (r < len(prices)):
            if (prices[r]>prices[l]):
                prof = prices[r] - prices[l]
                res = max(res, prof)
            else:
                l=r
            r += 1
        return res

        #optimal soln:-
        # maxP = 0
        # minBuy = prices[0]

        # for sell in prices:
        #     maxP = max(maxP, sell - minBuy)
        #     minBuy = min(minBuy, sell)
        # return maxP
        

if __name__=="__main__":
    sol = Solution()
    prices = [10,1,5,6,7,1]
    print(sol.maxProfit(prices=prices))
        