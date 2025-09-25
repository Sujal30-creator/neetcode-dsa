# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         hash = dict()
#         final_list = list()
#         list_1 = list()
#         sol_list = list()
#         list_2 = list()
                
#         for i in range(len(strs)):
#             list_1.append("".join(sorted(strs[i])))
        

#         def value(m: str, n: list):
#             ind_key = list()
#             for i,v in enumerate(n):
#                 if v == m:
#                     ind_key.append(int(i))
                
#             # for x in ind_key:
#             #     ans = list_2.append(strs[x])

            
#             return ind_key



#         for j in range(len(list_1)):
#             if list_1[j] in final_list:
#                 pass
#             else:
#                 key = list_1.count(list_1[j])
#                 val = value(list_1[j],list_1)
                
#                 hash.update({key : val})
#                 final_list.append(list_1[j])
#                 sol_hash = dict(sorted(hash.items()))

#         def join(v:list):
#             ans=list()
#             for i in v:
#                 ans.append(strs[i])
#             return ans

#         for x,v in sol_hash.items():
#             hope = join(v)
#             sol_list.append(hope)
        

#         # for x,v in sol_hash.items():
#         #     # finale = [join(x, v)]
#         #     for i in v:
#         #         sol_list.append([strs[i]])

        
                

#         print(sol_list)
                        



# if __name__=='__main__':
#     sol = Solution()
#     strs = ["act","pots","tops","cat","stop","hat"]
#     sol.groupAnagrams(strs)

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))  # sort to create the key
            anagrams[sorted_word].append(word)   # group anagrams together

        return list(anagrams.values())  # return only the grouped values
    
if __name__=='__main__':
    sol = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    sol.groupAnagrams(strs)
