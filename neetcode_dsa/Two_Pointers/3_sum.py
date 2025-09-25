class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # sum_arr = []

        # nums.sort()

        # if ((len(nums)>=3) & (len(nums)<=1000)):
        #     for i in range(len(nums)):
        #         if i>0 and nums[i] == nums[i-1]:
        #             continue
        #         target = nums[i]

        #         right = len(nums)-1

                
        #         left = i+1

        #         while (left<right):
        #             current_sum = nums[right]+nums[left]+target
                    
        #             if (current_sum == 0):
        #                 sum_arr.append([target, nums[left], nums[right]])
        #                 left += 1
        #                 right -= 1
        #                 # Move past duplicates
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1

        #             elif current_sum > 0:
        #                 right -= 1
        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1

        #             else: # current_sum < 0
        #                 left += 1
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
                    
                        
        # else:
        #     return []
        # return sum_arr
        sum_arr = []
        nums.sort()

        #start the loop
        for i in range(len(nums)):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            #initialize the variables
            target = nums[i]
            left = i+1
            right = len(nums)-1

            while (left<right):
                curr_sum = target+nums[left]+nums[right]

                if (curr_sum == 0):
                    sum_arr.append([target,nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1

                    while left<right and nums[right] == nums[right+1]:
                        right-=1

                elif (curr_sum > 0):
                    right -= 1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1

                else:
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1

        return sum_arr


if __name__=="__main__":
    sol = Solution()
    strs = [-2,0,1,1,2]
    print(sol.threeSum(strs))


#      
           