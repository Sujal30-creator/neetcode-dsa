class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        i,j = 1, 0
        count = 0
        while j == len(nums):
            if sum(nums[j:i]) == k:
                print(f'Summed up array: {nums[j:i]} and sum is {sum(nums[j:i])}')
                count += 1
            elif sum(nums[j:i]) > k:
                print(f'The sum val exceeded for subarr: {nums[j:i]}')
                j += 1
            i+=1

        return count
    
if __name__=="__main__":
    sol = Solution()
    print(sol.subarraySum(nums=[2,-1,1,2], k=2))

