class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def _sorted_insert(self, head, node):
        if head is None or node.date < head.data:
            node.next = head
            return node
        
        current = head

        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node

        return head
    
    def merge_sorted_lists(self, other_list):
        dummy = Node(0)
        tail = dummy

        left = self.head
        right = other_list.head

        while left is not None and right is not None:
            if left.data < right.data:
                tail.next = leftleft = left.next
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left is not None else right
        self.head = dummy.next
