"""
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_linked_list(l):
    if len(l) == 0:
        return None
    else:
        linked_list = ListNode(l[0])
        cur_node = linked_list

        for idx in range(1, len(l)):
            while cur_node.next != None:  # 마지막 노드까지 도달하게 하는 구문
                cur_node = cur_node.next
            cur_node.next = ListNode(val=l[idx])
        return linked_list


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1:
        :param l2:
        :return:
        """

        next_node_1 = l1
        next_node_2 = l2
        s_1 = ""
        s_2 = ""
        while next_node_1:
            s_1 += str(next_node_1.val)
            next_node_1 = next_node_1.next

        while next_node_2:
            s_2 += str(next_node_2.val)
            next_node_2 = next_node_2.next

        s_1 = s_1[::-1]
        s_2 = s_2[::-1]
        _sum = str(int(s_1) + int(s_2))[::-1]
        out = [ch for ch in _sum]
        return self.make_linked_list(out)

    def make_linked_list(self, l):
        if len(l) == 0:
            return None
        else:
            linked_list = ListNode(l[0])
            cur_node = linked_list

            for idx in range(1, len(l)):
                while cur_node.next != None:  # 마지막 노드까지 도달하게 하는 구문
                    cur_node = cur_node.next
                cur_node.next = ListNode(val=l[idx])
            return linked_list

# solver = Solution()
#
# T_1_a = make_linked_list([2, 4, 3])
# T_1_b = make_linked_list([5, 6, 4])
# print(solver.addTwoNumbers(T_1_a, T_1_b))
#
# T_2_a = make_linked_list([0])
# T_2_b = make_linked_list([0])
# print(solver.addTwoNumbers(T_2_a, T_2_b))
#
# T_3_a = make_linked_list([9, 9, 9, 9, 9, 9, 9])
# T_3_b = make_linked_list([9, 9, 9, 9])
# print(solver.addTwoNumbers(T_3_a, T_3_b))