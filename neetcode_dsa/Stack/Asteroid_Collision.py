class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = list()
        for asteroid in asteroids:
            if stack:
                val = stack[-1]

                if val>0 and asteroid<0:
                    #if asteroid is -ve and val is +ve ---> keep on poping the stack value until the val is greter than the asteroid value
                    if val>0 and asteroid<0:
                        if abs(val) == abs(asteroid):
                            stack.pop()
                            continue
                        while stack and abs(asteroid) > abs(stack[-1]):
                            stack.pop()

                            if stack and stack[-1] < 0:
                                stack.append(asteroid)
                                break
                    
                    if not stack:
                            stack.append(asteroid)
                else:
                    stack.append(asteroid) 
            else:
                stack.append(asteroid)

            print(stack)
        return stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision(asteroids=[-2, -2, 1, -2]))