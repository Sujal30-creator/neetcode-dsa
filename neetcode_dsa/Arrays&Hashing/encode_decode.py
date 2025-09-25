# class Solution:
#     def encode(self, strs: list[str]) -> str:
#         s = ""
#         for i in strs:
#             lth = 0
#             lth = len(i)
#             s = s + "".join(str(lth) + "#" + str(i))
#         print(str(s))

#         decoded = self.decode(s)
#         return decoded


        

#     def decode(self, s: str) -> list[str]:
#         nums = ['0','1','2','3','4','5','6','7','8','9']
#         s = [ch for ch in s if ch not in nums]
#         sol = []
#         result=[]

#         for i in s:
#             if i == '#':
#                 if len(sol)>=1:
#                      result.append("".join(sol))
#                 sol=[]
#             else:
#                 sol.append(i)

#         result.append("".join(sol))
                
#         return result

    

# if __name__ == '__main__':
#     sol = Solution()
#     strs = []
#     print(sol.encode(strs))

class Solution:
    def encode(self, strs: list[str]) -> str:
        s = ""
        for i in strs:
            s += f"{len(i)}#{i}"
        return s

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the separator '#'
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res

if __name__ == '__main__':
    sol = Solution()
    strs = ["neet", "code", "love", "you"]
    encoded = sol.encode(strs)
    print("Encoded:", encoded)
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)