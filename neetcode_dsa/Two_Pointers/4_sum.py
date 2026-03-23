class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        sum_arr = list()
        nums.sort()

        start, end = 0, len(nums)-1
        
        while start< end:
            left, right = start+1, end-1
            while left<right:
                curr_sum = nums[start] + nums[end] + nums[left] + nums[right]

                if curr_sum == target:
                    sum_arr.append([nums[start], nums[left], nums[end], nums[right]])
                    start+=1
                    end-=1
                elif curr_sum > target:
                    if right == left + 1:
                        end -=1
                    else:
                        right -= 1
                else:
                    if left == right-1:
                        start += 1
                    else:
                        left+=1


        # start, end = 0, len(nums)-1

        # left, right = start+1, end-1

        # while start<len(nums)-4:
        #     while left<right:
        #         curr_sum = nums[start] + nums[end] + nums[left] + nums[right]
        #         if curr_sum == target:
        #             sum_arr.append([nums[start], nums[left], nums[end], nums[right]])
                
        #         if right == left+1 and end == right+1:
                    
                    
        return sum_arr

if __name__=="__main__":
    sol = Solution()
    print(sol.fourSum(nums=[-3,-1,0,2,4,5], target = 0))