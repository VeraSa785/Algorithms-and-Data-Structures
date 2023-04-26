class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

my_linked_list = LinkedList(4)
my_linked_list.append(3)
# my_linked_list.print_list()

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
                                                                                                                    