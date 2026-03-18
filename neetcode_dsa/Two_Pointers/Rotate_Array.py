class Solution:
    def rotate(self, nums: list[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1

        for _ in range(k):
            val = nums.pop(right)
            nums.insert(0,val)
        
        return nums


if __name__=="__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(sol.rotate(nums,k))