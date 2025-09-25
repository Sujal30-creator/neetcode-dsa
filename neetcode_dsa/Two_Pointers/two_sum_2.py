class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers)-1

        while (start<end):
            if (numbers[start] + numbers[end] == target):
                return (start+1, end+1)
            elif (numbers[start] + numbers[end] > target):
                end -= 1
            else:
                start += 1
        
        return [-1,-1]

if __name__=="__main__":
    sol = Solution()
    strs = [1,2,3,4]
    target = 3
    print(sol.twoSum(strs,target))

        