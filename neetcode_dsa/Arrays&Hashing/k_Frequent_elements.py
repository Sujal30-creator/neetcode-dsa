from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return [item for item,freq in count.most_common(k)]

if __name__=='__main__':
    sol = Solution()
    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    print(sol.topKFrequent(nums, k))