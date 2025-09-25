class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in matrix:
            if (i[0]<=target) and (i[len(i)-1]>=target) :
                start,end = 0, len(i)-1

                while start<=end:
                    middle = (start+end) // 2

                    if (i[middle]==target):
                        return True
                    elif (i[middle] > target):
                        end = middle-1
                    elif (i[middle]<target):
                        start = middle+1
        return False 


if __name__=="__main__":
    sol = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 15
    print(sol.searchMatrix(matrix=matrix,target=target))
        