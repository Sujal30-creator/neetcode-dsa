class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        pair.sort(key=lambda x:x[0],reverse=True)
        stack = []

        for p,s in pair:
            time = (target-p) / s

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



if __name__=="__main__":
    sol = Solution()
    print(sol.carFleet(target=12,position=[10,8,0,5,3],speed=[2,4,1,1,3]))