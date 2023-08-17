"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]            #saving the head as list to run the related function about queue 

    def enqueue(self, new_element):
        self.storage.append(new_element) #using append method to add the new element to the end of the list
        return
    def peek(self):
        return self.storage[0]           # 0 is for showing the first item in list
    def dequeue(self):
        return self.storage.pop(0)       # using pop(0) to return first item in list
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
