
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newhead = None
        current = newhead

        while head:
            if head.val != val:
                if newhead != None:
                    newhead = ListNode(head.val)
                    current = newhead
                else:
                    current.next = ListNode(head.val)
                    current = current.next
            head = head.next

        return newhead

