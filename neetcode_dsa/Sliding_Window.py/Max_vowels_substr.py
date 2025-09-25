class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        holder = [c in {'a','e','i','o','u'} for c in s]

        count=maxcount=sum(holder[:k])

        for i in range(len(holder)-k):
            count = count + (holder[i+k]-holder[i])
            if count>maxcount:
                maxcount=count
        return maxcount

if __name__=='__main__':
    sol = Solution()
    print(sol.maxVowels(s='abciiidef',k=3))