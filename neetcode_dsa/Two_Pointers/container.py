class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0

        while(left<right):
            width = right-left
            min_height = min(heights[right],heights[left])

            curr_area = min_height*width
            max_area = max(max_area,curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
                           


if __name__=="__main__":
    sol = Solution()
    strs = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
    print(sol.maxArea(strs))