# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Use the dummy head pattern to build the result list
        dummy_head = ListNode()
        tail = dummy_head

        carry = 0

        # Loop until both lists are exhausted AND there is no carry left
        while l1 is not None or l2 is not None or carry != 0:
            # Get the value from the l1 node, or 0 if l1 is done
            val1 = l1.val if l1 is not None else 0
            # Get the value from the l2 node, or 0 if l2 is done
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum for this "column"
            column_sum = val1 + val2 + carry

            # The new digit is the remainder
            new_digit = column_sum % 10
            # The new carry is the integer division
            carry = column_sum // 10

            # Create the new node and append it to our result list
            new_node = ListNode(new_digit)
            tail.next = new_node

            # Advance all the pointers
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy_head.next