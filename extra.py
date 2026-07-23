'''
Input's are :
n = length of the array
arr = array itself
F/f/L/l = first/ last
'''

class Solution:
    def lumotoSwap(self, nums: list) -> list:
        pivot = nums.pop()
        swapped_list = [str(pivot)]
        ctr = 1

        for i in range(len(nums)):
            if nums[i] > pivot:
                swapped_list.insert(ctr,str(nums[i]))
            else:
                swapped_list.insert(ctr-1, str(nums[i]))
                ctr+=1

        return swapped_list


if __name__=="__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split(',')))
    order = input().strip()

    if order == "L" or order == "l":
        ans = sol.lumotoSwap(arr)
    elif order == "F" or order == "f":
        arr[0], arr[-1] = arr[-1], arr[0]
        ans = sol.lumotoSwap(arr)
    print(", ".join(ans))



