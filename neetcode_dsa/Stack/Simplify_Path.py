class Solution:
    def simplifyPath(self, path: str) -> str:
        # line_char = '/'
        # dot_char = '.'
        # stack = list()

        # for i in range(len(path)):
        #     if i == 0 and path[i] == '/':
        #         print(f'put the first character --> {path[i]}')
        #         stack.append(path[i])
        #     elif i != 0 and stack:
        #         if path[i] == line_char:
        #             #Check the value of stack[-1], if it's a line char => continue or else append
        #             if stack[-1] == line_char:
        #                 continue
        #             else:
        #                 stack.append(path[i])
                
        #         elif path[i] == dot_char:
        #             #Check if the stack[-1] is the initial line char if it is return only the line char or else pop() from the stack.
        #             if stack[-1] == line_char or stack[-1] == dot_char:
        #                 val = stack.pop()
        #                 if not stack:
        #                     stack.append(val)
        #             else:
        #                 stack.pop()
                
        #         else:
        #             #Check if stack[-1] is a char => add the before characters else is a line char => append it
        #             if stack[-1] == line_char:
        #                 stack.append(path[i])
        #             else:
        #                 char = stack.pop()
        #                 char += path[i]
        #                 stack.append(char)

                     
        #     else:
        #         print('Invalid')
        
        # if stack[-1] == line_char:
        #         extra = stack.pop()
        #         if not stack:
        #             stack.append(extra)

        # return ''.join(stack)
        stack = list()

        for char in path.split("/"):
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "/"+"/".join(stack)

if __name__=="__main__":
    sol = Solution()
    print(sol.simplifyPath(path="/home/user/Documents/../Pictures"))