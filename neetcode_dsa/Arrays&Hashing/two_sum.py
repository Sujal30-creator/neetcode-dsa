class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = dict()

        for index,value in enumerate(nums):
            
            difference = target-value
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[value] = index
            print(hashmap)
    
        return []
        
    
if __name__=='__main__':
    sol = Solution()
    nums = [10,13,9,20]
    target = 19
    outcome = sol.twoSum(nums,target)
    print(outcome)

 
        