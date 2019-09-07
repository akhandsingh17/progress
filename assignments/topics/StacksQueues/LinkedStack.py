from assignments.assignments.topics.StacksQueues.EmptyException import EmptyStackException

""" LIFO stack implemention using a singly linked list for storage """
class LinkedStack:
    """ nested nonpublic class _None """
    class _Node:
        def __init__(self, element: int, next: "_Node" = None):
            self._element = element
            self._next = next

        def __repr__(self):
            return "Node <{}>".format(self.value)

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self) -> bool:
        return self._size == 0

    def push(self, e: int) -> None:
         self._head = self._Node(e, self._head)
         self._size += 1

    def top(self) -> int:
        if self.isEmpty():
            raise EmptyStackException('Stack is empty')
        else:
            return self._head._element

    def pop(self) -> int:
        if self.isEmpty():
            raise EmptyStackException('Stack is empty')
        else:
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1
            return answer

if __name__ == "__main__":
    MyStack = LinkedStack()
    MyStack.push(11)
    print(MyStack.top())

