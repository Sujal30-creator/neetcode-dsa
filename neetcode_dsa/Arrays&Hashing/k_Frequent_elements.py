class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)


        print(count)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        print(arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        return res

if __name__=='__main__':
    sol = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    print(sol.topKFrequent(nums, k))