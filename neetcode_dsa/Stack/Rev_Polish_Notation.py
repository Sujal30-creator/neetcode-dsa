class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands = ["+","-","*","/"]
        stack = []

        for char in tokens:
            if char in operands:
                opr_2 = int(stack.pop())
                opr_1 = int(stack.pop())
                print(opr_1,opr_2)
                if char == "+":
                    res = opr_1 + opr_2
                elif char == "-":
                    res = opr_1 - opr_2
                elif char == "*":
                    res = opr_1 * opr_2
                else:
                    res = opr_1 / opr_2
                stack.append(res)
            else:
                stack.append(char)

        return int(stack.pop())
    
if __name__=="__main__":
    sol = Solution()
    print(sol.evalRPN(tokens=["0","3","/"]))
        