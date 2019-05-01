class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class ssl:

    def __init__(self):
        self.head = Node()

    def display(self):
        if self.head.data == None:
            print "List is empty"
            elems = []
        else:
            curr = self.head
            elems = [curr.data]
            while curr.next != None:
                curr = curr.next
                elems.append(curr.data)
        return elems

    def length(self):
        if self.head.data == None:
            return 0
        else:
            curr = self.head
            l = 1
            while curr.next != None:
                l += 1
                curr = curr.next
            return l

    def append(self, data):
        new_node = Node(data=data)
        if self.head.data == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def prepend(self, data):
        if self.head.data == None:
            self.head =  Node(data=data)
        else:
            self.head = Node(data=data, next=self.head)

    def insert_val(self, data, prev="NA", post="NA"):
        if self.length() >= 2:
            p_prev = self.head
            p_post = p_prev.next
            while p_post != None:
                if p_prev.data == prev and p_post.data == post:
                    p_prev.next = Node(data=data, next=p_post)
                    print "Value inserted"
                    break
                else:
                    p_prev = p_post
                    p_post = p_post.next
            else:
                print "Error: not found the given values in a serial. Could not insert."

        else:
            print "Error: there are <2 values in the list. cannot insert and try with append/prepend"

    def insert_index(self, data, index):
        if index > self.length() or index < 0:
            print "Error: invalid index"
        else:
            if index == 0:
                self.head = Node(data=data, next=self.head.next)
            else:
                i = 1
                prev = self.head
                curr = self.head.next
                while curr.data != None:
                    if i == index:
                        prev.next = Node(data=data, next=curr)
                        print "Inserted a value at the given index value"
                        break
                    else:
                        i += 1
                        prev = curr
                        curr = curr.next

    def delete_val(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while curr.data != None:
                if curr.data == data:
                    prev.next = curr.next
                    print "Deleted the given value"
                    break
                else:
                    prev = curr
                    curr = curr.next
            else:
                print "Error: not found the given value. Could not delete."


    def delete_index(self, index):
        if index > self.length() or index < 0:
            print "Error: invalid index"
        else:
            if index == 0:
                self.head = self.head.next
            else:
                i = 1
                prev = self.head
                curr = self.head.next
                while curr.data != None:
                    if i == index:
                        prev.next = curr.next
                        print "Deleted a value at the given index value"
                        break
                    else:
                        i += 1
                        prev = curr
                        curr = curr.next
                else:
                    print "Error: not found the given value. Could not delete."


sl = ssl()
for each in dir(sl):
    print "sl.%s()"%(each)
import pdb
pdb.set_trace()