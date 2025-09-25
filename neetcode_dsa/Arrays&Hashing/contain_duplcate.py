class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = dict()
        sol_list = list()

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
                
        
        print(hashmap)
        keys = hashmap.keys()
        print(keys)
        for k in keys:
            if hashmap[k] > 1:
                return True
        return False

    
        
if __name__=='__main__':
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))