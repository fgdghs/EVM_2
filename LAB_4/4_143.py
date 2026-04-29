class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_curr = slow.next
        slow.next = None

        prev_node = None
        while right_curr:
            next_temp = right_curr.next
            right_curr.next = prev_node
            prev_node = right_curr
            right_curr = next_temp

        left_ptr = head
        right_ptr = prev_node

        while right_ptr:
            left_next = left_ptr.next
            right_next = right_ptr.next

            left_ptr.next = right_ptr
            right_ptr.next = left_next

            left_ptr = left_next
            right_ptr = right_next
