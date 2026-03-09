class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
            
        rows, cols = len(matrix), len(matrix[0])
        # Create a prefix sum matrix padded with an extra row and column of zeros
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build the prefix sum array
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix[r][c + 1] 
                    + self.prefix[r + 1][c] 
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the result using the precomputed prefix sums in O(1) time
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
    
    #My Solution -------> Passed on Neetcode but TLE on Leetcode
    #     def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
        

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sliced_matrix = self.matrix[row1:row2+1]
    #     print(sliced_matrix)
    #     matrix_sum =0
    #     for i in range(len(sliced_matrix)):
    #         matrix_sum += sum(sliced_matrix[i][col1:col2+1])

    #     return matrix_sum

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)