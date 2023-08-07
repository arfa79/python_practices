<<<<<<< HEAD
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head                # create head varriable to find nodes position and modify them 

    def append(self, new_element):      
        current = self.head             # we make a varriable and do it equal to head for better handeling the position of nodes
        if self.head:
            while current.next:         # create a always true loop for execute the function  
                current = current.next  # going to the next node with .next method
            current.next = new_element  # make equal new and current elements for replacing current with new  
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1                           # make a counter for indexing and using in conditions
        while current and count < position: #comparing to count and current node to find position  
            current = current.next      
            count += 1                      # when function get this node plus one to know how much it get

        if current:
            return current
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:                          #first position
            new_element.next = self.head           #head is going forward in place of next element for inserting the newelement 
            self.head = new_element
        else:
            prev = self.get_position(position - 1) # using get position class to find previous position --> position - 1 
            if prev:
                new_element.next = prev.next       # inserting new element
                prev.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None

        while current:
            if current.value == value:       
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                break
            prev = current         # making equal to none for deleting 
            current = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
=======
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head                # create head varriable to find nodes position and modify them 

    def append(self, new_element):      
        current = self.head             # we make a varriable and do it equal to head for better handeling the position of nodes
        if self.head:
            while current.next:         # create a always true loop for execute the function  
                current = current.next  # going to the next node with .next method
            current.next = new_element  # make equal new and current elements for replacing current with new  
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1                           # make a counter for indexing and using in conditions
        while current and count < position: #comparing to count and current node to find position  
            current = current.next      
            count += 1                      # when function get this node plus one to know how much it get

        if current:
            return current
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:                          #first position
            new_element.next = self.head           #head is going forward in place of next element for inserting the newelement 
            self.head = new_element
        else:
            prev = self.get_position(position - 1) # using get position class to find previous position --> position - 1 
            if prev:
                new_element.next = prev.next       # inserting new element
                prev.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None

        while current:
            if current.value == value:       
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                break
            prev = current         # making equal to none for deleting 
            current = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
>>>>>>> 7e73418abf2b1142fe39f38c5b2a0f6626261581
