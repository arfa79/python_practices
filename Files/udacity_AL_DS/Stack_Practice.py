class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head  # like a linked list use a varriable to equal to the head and then equal to new element for replace 
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"
        if self.head:
            deleted_element = self.head    # store head as deleted_element 
            self.head = self.head.next     # going forward with the head and delete with this action
            deleted_element.next = None    # remove the link of the elment for making sure delete it complitely
            return deleted_element
        else:
            return None

class Stack:
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
