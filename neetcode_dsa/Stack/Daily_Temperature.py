class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = list()

        for index,value in enumerate(temperatures):
            if not stack:
                stack.append([value,index])
            else:
                while stack and value>stack[-1][0]:
                    stackVal, stackInd = stack.pop()
                    res[stackInd] = (index - stackInd)

                stack.append([value,index])
        return res


if __name__=="__main__":
    sol = Solution()
    daily_temperatures = [73,74,75,71,69,72,76,73]
    print(sol.dailyTemperatures(temperatures=daily_temperatures))
        