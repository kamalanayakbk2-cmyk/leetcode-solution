# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node_1=l1
        cur_node_2=l2
        dummy_head=ListNode()
        tmp_sum_node=dummy_head

        add_one=False
        while cur_node_1 or cur_node_2:
            tmp_sum_node.next=ListNode()
            tmp_sum_node=tmp_sum_node.next
            value_1=cur_node_1.val if cur_node_1 else 0
            value_2=cur_node_2.val if cur_node_2 else 0
            cur_sum = value_1 + value_2 + add_one
            if cur_sum >= 10:
                add_one=True
                cur_digit=cur_sum % 10
            else:
                cur_digit=cur_sum
                add_one=False
            tmp_sum_node.val=cur_digit
            if cur_node_1:   
                cur_node_1=cur_node_1.next
            if cur_node_2:
                cur_node_2=cur_node_2.next
        if add_one:
            tmp_sum_node.next=ListNode(val=1)
        return dummy_head.next




