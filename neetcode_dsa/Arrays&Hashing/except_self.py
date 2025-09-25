class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        sol = list()

        def returnsum(num:int,arr:list):
            if len(arr) == 1:
                return 0

            sumnum = 1
            for x in range(len(arr)):
                if x == num:
                    pass
                else:
                    sumnum *= arr[x]
            
            return sumnum


        for i in range(len(nums)):
            sol.append(returnsum(i,nums))

        return sol

if __name__ == '__main__':
    sol = Solution()
    nums = [0]
    print(sol.productExceptSelf(nums))
