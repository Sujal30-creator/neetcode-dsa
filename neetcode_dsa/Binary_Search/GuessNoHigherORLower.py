# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n

        while start<=end:
            middle = (start+end) // 2

            ans = guess(middle)

            if (ans == 0):
                return middle
            elif (ans == -1):
                end = middle-1
            else:
                start = middle+1
        return -1
        