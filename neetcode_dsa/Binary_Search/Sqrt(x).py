import math

class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, x

        while (start<=end):
            middle = (start+end) // 2
            val = math.floor(x/middle)

            print(f'middle: {middle}, val: {val}')
            if (val==middle):
                return middle
            elif (val<middle):
                end = middle-1
            else:
                start = middle+1    
        return start-1

if __name__=="__main__":
    sol = Solution()
    print(sol.mySqrt(x=18))