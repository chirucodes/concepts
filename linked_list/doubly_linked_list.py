class Node:
    def __init__(self, data=None, prev_a=None, next_a=None):
        self.data = data
        self.prev_a = prev_a
        self.next_a = next_a

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data=data)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print type(new_node)
            print dir(new_node)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            while curr.next_a != None:
                curr = curr.next_a
            curr.next_a = Node(data=data, prev_a=curr)
            self.tail = curr.next_a

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data=data)
            self.tail = self.head
        else:
            new_node = Node(data=data, next_a=self.head)
            self.head.prev_a = new_node
            self.head = new_node

    def insert(self,data, prev_val, next_val):
        if self.length() >= 2:
            print "The list has >=2 nodes, proceeding with insertion"
            next =  self.head.next_a
            if self.head.data == prev_val and next.data == next_val:
                new_node = Node(data=data, prev_a=next.prev_a, next_a=self.head.next_a)
                self.head.next_a = new_node
                next.prev_a = new_node
            else:
                curr = self.head
                prev = self.head
                next = self.head.next_a
                while curr.next_a != None:
                    if prev.data == prev_val and next.data == next_val:
                        new_node = Node(data=data, prev_a=next.prev_a, next_a=self.head.next_a)
                        self.head.next_a = new_node
                        next.prev_a = new_node
                    else:
                        prev = curr
                        curr = curr.next_a
                        next = self.head.next_a
        else:
            print "The list has <2 nodes, please do append/prepend"

    def length(self):
        if self.head == None:
            print "Length: 0"
            return 0
        else:
            curr = self.head
            l = 1
            while curr.next_a != None:
                curr = curr.next_a
                l += 1
            print "Length: ",l
            return l

    def delete_val(self, data):
        length = self.length()
        if length == 0:
                print "Value not found"
        elif length == 1:
            if self.head.data == data:
                self.head = None
                self.tail = None
                print "Deleted first element"
        elif length > 1:
            if self.head.data == data:
                self.head = self.head.next_a
                print "Deleted first element"
            if self.tail.data == data:
                self.tail = self.tail.prev_a
                self.tail.next_a = None
                print "Deleted tail element"
            else:
                prev = self.head
                curr = prev.next_a
                while curr.next_a != None:
                    next = curr.next_a
                    if curr.data == data:
                        print "Not a first element, deleting..."
                        prev.next_a = curr.next_a
                        next.prev_a = curr.prev_a
                        if curr.next_a == None:
                            self.tail = curr
                        break
                    prev = curr
                    curr = curr.next_a

    def display(self):
        if self.head == None:
            print "List is empty"
        else:
            curr = self.head
            elems = [curr.data]
            while curr.next_a != None:
                curr = curr.next_a
                elems.append(curr.data)
            print "Display: ", elems

    def display_in_reverse(self):
        if self.tail == None:
            print "List is empty"
        else:
            curr = self.tail
            elems = [curr.data]
            while curr.prev_a != None:
                curr = curr.prev_a
                elems.append(curr.data)
            print "Display in reverse order: ", elems



dl=dll()
for each in dir(dl):
    print "dl.%s()"%each
import pdb
pdb.set_trace()
