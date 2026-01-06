#Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.curr = None

    def reverseList(self, head: list) -> list:
        if len(head) == 0:
            return []
        else:
            for i in range(len(head)):
                newNode = ListNode(head[i])
                newNode.next = self.curr
                self.curr = newNode

        nums = []
        current = self.curr
        while current:
            nums.append(current.val)
            current = current.next
        
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseList(head=[0,1,2,3,4]))
        
        