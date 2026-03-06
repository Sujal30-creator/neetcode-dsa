class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = dict()

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        max_ele = [int,0]

        for key, value in hashmap.items():
            if value > max_ele[1]:
                max_ele[1] = value
                max_ele[0] = key
        
        return max_ele[0]
    

if __name__=="__main__":
    sol = Solution()
    print(sol.majorityElement([2,2,1,1,1,2,2]))
        

        