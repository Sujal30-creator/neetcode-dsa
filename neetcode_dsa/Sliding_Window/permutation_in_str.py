class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        count = dict()
        for i in s1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1


        L = R = 0
        EP = len(s1) - 1
        hashmap = dict()

        for R in range(len(s2)):

            if s2[R] in hashmap:
                hashmap[s2[R]] += 1
            else:
                hashmap[s2[R]] = 1

            if EP == R :

                if hashmap == count :
                    return True
                EP += 1
                hashmap[s2[L]] -= 1
                if hashmap[s2[L]] == 0:
                    del hashmap[s2[L]]
                L+=1
            
        return False


        # l= 0
        # r = l + len(s1)-1
        # hashmap = dict()
        
        # for l in range(len(s2)):
        #     if r-l <= (len(s1)-1) :
        #         if r>=l :
        #             if s2[l] in hashmap:
        #                 hashmap[s2[l]] += 1
        #             else:
        #                 hashmap[s2[l]] = 1

        #             if r == l:
        #                 hashmap = dict(sorted(hashmap.items()))
        #                 print(hashmap)
        #                 print(count)
        #                 if hashmap == count:
        #                     return True
                        
        #                 elif r != len(s2)-1:
        #                     r = r+len(s1)
        #                     hashmap = dict()
            
        #     else:
        #         return False
        
        # return False
                    

                    


        # for l in range(len(s2)):
        #     if s2[l] in count:
        #         if count[s2[l]]>0 and r>l:
        #             count[s2[l]] -= 1
        #         elif count[s2[l]]>0 and r==l:
        #             count[s2[l]]-=1
        #             return True
        #         else:
        #             return False
        #     else:
        #         r+=1

        # return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion(s1 = "abc", s2 = "lecabee"))