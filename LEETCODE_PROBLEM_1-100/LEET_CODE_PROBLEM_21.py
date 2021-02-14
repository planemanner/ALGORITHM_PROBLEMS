"""
Merge two sorted linked lists and return it as a sorted list.

The list should be made by splicing together the nodes of the first two lists.

Example.1)
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example.2)
Input: l1 = [], l2 = []
Output: []

Example.3)
Input: l1 = [], l2 = [0]
Output: [0]

Constraints

1.) The number of nodes in both lists is in the range [0, 50].
2.) -100 <= Node.val <= 100
3.) Both l1 and l2 are sorted in non-decreasing order. (Key-point)

list.next.next.next....이 가능하게.

답 쉽게 볼거면 solution 내에 return 파트의 make_linked_list를 지우면 됨.

Solution에 대한 평가: 평범한 Solution. 중상위 공간 복잡도, 중하위 시간 복잡도.

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

    def mergeTwoLists(self, l1, l2):
        cur_node_1 = l1
        cur_node_2 = l2
        sorted_list = []
        _max = 0
        if cur_node_1 == None and cur_node_2 == None:
            return self.make_linked_list(sorted_list)

        elif cur_node_1 != None and cur_node_2 == None:
            while cur_node_1 != None:
                sorted_list += [cur_node_1.val]
                cur_node_1 = cur_node_1.next
            return self.make_linked_list(sorted_list)

        elif cur_node_1 == None and cur_node_2 != None:
            while cur_node_2 != None:
                sorted_list += [cur_node_2.val]
                cur_node_2 = cur_node_2.next
            return self.make_linked_list(sorted_list)

        else:

            while not (cur_node_1 == None and cur_node_2 == None):

                left = cur_node_1.val if cur_node_1 != None else _max

                right = cur_node_2.val if cur_node_2 != None else _max

                if left < right:
                    _max = right
                    sorted_list += [left] if cur_node_1 != None else []

                    if cur_node_1 != None:
                        cur_node_1 = cur_node_1.next

                elif left == right:

                    if cur_node_1 != None:
                        sorted_list += [left]
                        _max = left
                        cur_node_1 = cur_node_1.next

                    if cur_node_2 != None:
                        sorted_list += [right]
                        _max = right
                        cur_node_2 = cur_node_2.next
                else:
                    _max = left
                    sorted_list += [right] if cur_node_2 != None else []

                    if cur_node_2 != None:
                        cur_node_2 = cur_node_2.next

            return self.make_linked_list(sorted_list)


a = make_linked_list([-9, 3])
b = make_linked_list([5, 7])
c = make_linked_list([2])
d = make_linked_list([1])
e = make_linked_list([1, 2, 4])
f = make_linked_list([1, 3, 4])
"""
Example.2)
Input: l1 = [], l2 = []
Output: []

Example.3)
Input: l1 = [], l2 = [0]
Output: [0]
"""
solver = Solution()
print(solver.mergeTwoLists(a, b))
# print(solver.mergeTwoLists(e, f))








