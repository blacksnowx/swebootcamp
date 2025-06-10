# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l1num = ""
        l2num = ""

        current_node = l1
        while current_node is not None:
            l1num += str(current_node.val)
            current_node = current_node.next

        current_node = l2
        while current_node is not None:
            l2num += str(current_node.val)
            current_node = current_node.next

        rev_l1num = l1num[::-1]
        rev_l2num = l2num[::-1]

        list_sum = str(int(rev_l1num) + int(rev_l2num))[::-1]
        print(list_sum)

        dummy_head = ListNode()

        tail = dummy_head

        for digit_char in list_sum:
            new_node = ListNode(int(digit_char))
            tail.next = new_node
            tail = tail.next

        return dummy_head.next
