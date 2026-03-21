class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ptr1, ptr2 = 0, 0
        dummy = list()
        nums1 = nums1[:m]
        nums2 = nums2[:n]

        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1] > nums2[ptr2]:
                dummy.append(nums2[ptr2])
                ptr2+=1
            elif nums1[ptr1] < nums2[ptr2]:
                dummy.append(nums1[ptr1])
                ptr1+=1
            elif nums1[ptr1] == nums2[ptr2]:
                dummy += [nums1[ptr1],nums2[ptr2]]
                ptr1+=1
                ptr2+=1

        if ptr1 == len(nums1):
            dummy += nums2[ptr2:n]
        elif ptr2 == len(nums2):
            dummy += nums1[ptr1:m]
        return dummy

if __name__=="__main__":
    sol = Solution()
    print(sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))