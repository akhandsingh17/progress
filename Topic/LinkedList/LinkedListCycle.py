class ListNode:
    def __init__(self, val, next = None):
        self._val = val
        self._next = next

    def __str__(self):
        return '(Value: {0}, Next: {1})'.format(self._val, self._next)

class Solution:
    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x._next) if x else []
        return '{' + '->'.join(traverse(self._head)) + '}'

    def hasCycle(self, head: ListNode) -> bool:
