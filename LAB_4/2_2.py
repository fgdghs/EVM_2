class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(val=(carry % 10))
            curr = curr.next

            carry //= 10

        if carry != 0:
            curr.next = ListNode(val=carry)

        return head.next
