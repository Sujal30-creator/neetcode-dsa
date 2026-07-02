class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = list()
        for asteroid in asteroids:
            if stack:
                val = stack[-1]

                # if val>=0 and asteroid>=0:
                #     stack.append(asteroid)
                # elif val<0 and asteroid<0:
                #     stack.append(asteroid)
                # elif val<0 and asteroid>0:
                #     if abs(val) > asteroid:
                #         stack.append(val)
                #     elif abs(val) == asteroid:
                #         stack.pop()
                #     else:
                #         stack.append(asteroid)
                # else:
                #     if abs(asteroid) > val:
                #         while stack and abs(asteroid) > stack[-1]:
                #             stack.pop()
                #         if not stack:
                #             stack.append(asteroid)
                #     else:
                #         continue

                if val>0 and asteroid < 0 or val<0 and asteroid > 0:
                    if val>0 and asteroid<0:
                        while stack and abs(asteroid) >= stack[-1]:
                            stack.pop()
                        if not stack:
                            stack.append(asteroid)
                        
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision(asteroids=[3,5,-6,2,-1,4]))