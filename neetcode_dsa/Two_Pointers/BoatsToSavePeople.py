class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ptr1 = 0
        ptr2 = 1
        count = 0

        while ptr1 < len(people)-2:
            if people[ptr1] == limit:
                count += 1
                ptr1+=1
                ptr2+=1
            elif people[ptr2] == limit:
                count+=1
                ptr2+=1
            elif people[ptr1]+people[ptr2] <= limit:
                count+=1
                ptr1=ptr2+1
                ptr2= ptr1+1
            else:
                ptr1

        if people[ptr1]+people[ptr2]<=limit:
            count+=2
        else:
            if people[ptr1] <= limit:
                count+=1
            if people[ptr2]<= limit:
                count+=1
            
        return count

if __name__=="__main__":
    sol = Solution()
    print(sol.numRescueBoats(people=[3,2,2,1],limit=3))
        
