class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()  # Sort the list
        # sol = []  # To store unique sorted numbers

        # # Remove duplicates
        # for i in nums:
        #     # if not sol or sol[-1] != i:
        #     #     sol.append(i)
        #     if i not in sol:
        #          sol.append(i)

        # max_len = 1  # At least one number in sequence
        # curr_len = 1

        # for i in range(1, len(sol)):
        #     if sol[i] == sol[i - 1] + 1:
        #         curr_len += 1
        #     else:
        #         max_len = max(max_len, curr_len)
        #         curr_len = 1  # Reset if not consecutive

        # return max(max_len, curr_len)  # Handle last sequence
        numSet = set(nums)
        longest = 0
        print(numSet)

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

            


if __name__ == '__main__':
    sol = Solution()
    strs = [2,20,4,10,3,4,5]
    print(sol.longestConsecutive(strs))
    
