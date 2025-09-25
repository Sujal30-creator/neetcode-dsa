class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start, end  = 0,1
        max_profit = 0

        while (end < len(prices)):
            if (prices[start]<prices[end]):
                current_profit = prices[end] - prices[start]
                max_profit = max(current_profit,max_profit)
            else:
                start=end
            end+=1
        
        return max_profit


if __name__=="__main__":
    sol = Solution()
    strs = [-1,0,1,2,-1,-4]
    print(sol.maxProfit(strs))
        