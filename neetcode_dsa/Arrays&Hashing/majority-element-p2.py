class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashmap = dict()
        ans = list()
        limit = len(nums) / 3

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        for key, value in hashmap.items():
            if value > limit:
                ans.append(key)

        return ans

if __name__=="__main__":
    sol = Solution()
    print(sol.majorityElement([5,2,3,2,2,2,2,5,5,5]))