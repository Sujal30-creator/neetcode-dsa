class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        i=0

        for _ in range(hashmap.get(0,0)):
            nums[i] = 0
            i+=1

        for _ in range(hashmap.get(1,0)):
            nums[i] = 1
            i+=1

        for _ in range(hashmap.get(2,0)):
            nums[i] = 2
            i+=1
        print(nums)
            

if __name__=="__main__":
    sol = Solution()
    sol.sortColors(nums=[1,0,1,2])