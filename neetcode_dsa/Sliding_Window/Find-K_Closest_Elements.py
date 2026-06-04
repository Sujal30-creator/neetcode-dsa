class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int):
        # L, R = 0, k-1
        # sum, num = 0, 0
        # hashmap =dict()

        # for i in range(len(arr)):
        #     if i <= R:
        #         num =  abs(arr[i] - x)
        #         sum = sum+num
        #         # print(f'Iteration {i} num = {num} sum={sum}')

        #         if i == R:
        #             if sum in hashmap:
        #                 continue
        #             else:
        #                 hashmap[sum] = arr[L:R+1]
        #             sum = sum - (abs(arr[L]-x))
        #             L+=1
        #             R+=1
            
        # min_key = min(hashmap.keys())
        # # print(f'final min_key = {min_key}, final hashmap = {hashmap}')
        # return hashmap[min_key]

        L, R = 0, len(arr)-1

        while R-L >= k:
            if abs(arr[L] - x) > abs(arr[R] - x):
                L+=1
            else:
                R-=1

        return arr[L:R+1] 

if __name__=="__main__":
    sol = Solution()
    nums_arr = [2,3,4]
    k = 3
    x = 1
    print(sol.findClosestElements(arr = nums_arr, k=k,x=x))