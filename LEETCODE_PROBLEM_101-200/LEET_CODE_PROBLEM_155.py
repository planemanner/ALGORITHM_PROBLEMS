"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

    Methods pop, top and getMin operations will always be called on non-empty stacks.

Runtime: 48 ms, faster than 89.33% of Python online submissions for Min Stack.
Memory Usage: 17.5 MB, less than 64.88% of Python online submissions for Min Stack.

Runtime: 52 ms, faster than 73.90% of Python online submissions for Min Stack.
Memory Usage: 17.4 MB, less than 87.07% of Python online submissions for Min Stack.

96.84 % time complexity, 44ms
64.88 % space complexity

Avg eval : 86.69 % time complexity
           72.28 % space complexity
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_idx = 0

        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.data) > 0:
            if self.data[self.min_idx] > x:
                self.min_idx = len(self.data)
        self.data += [x]

    '''"push", "getMin", "pop", "getMin"'''
    def pop(self):
        """
        :rtype: None
        """
        top_val = self.data[-1]

        if top_val == self.data[self.min_idx]:
            if len(self.data) == 2:
                self.min_idx = 0
            elif len(self.data) > 2:
                new_idx = len(self.data) - 2
                for i in range(len(self.data)-1):
                    if self.data[i] < self.data[new_idx]:
                        new_idx = i
                self.min_idx = new_idx
            else:
                pass

        del self.data[-1]

        return top_val

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        -> in constant time.
        :rtype: int
        """
        return self.data[self.min_idx]





