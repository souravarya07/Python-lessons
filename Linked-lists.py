#Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Implementing Queue using Linked lists
class CustomQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def enqueue(self,value):
        node = Node(value)
        if self.start is None:
            self.start = node
        else:
            self.end.next = node
        self.end = node
        self.size += 1

    def dequeue(self):
        if self.start == None:
            return None
        elif self.start == self.end:
            removed_value = self.start
            self.start = None
            self.end = None
            self.size -= 1
            return removed_value
        else:
            returned_value = self.start
            self.start = self.start.next
            returned_value.next = None
            self.size -= 1
            return returned_value

    def is_empty(self):
        return self.size == 0
    def qsize(self):
        return self.size

    def front(self):
        if self.start==None:
            return None
        else:
            return self.start.value

    def last(self):
        if self.end == None:
            return None
        else:
            return self.end.value

    def __str__(self):
        result = "["
        i = self.start
        while i is not None:
            result += str(i.value)
            result += ", "
            i = i.next
        result += "]"
        return result



#Implementing stacks using Linked lists:
class CustomStack:
    def __init__(self):
        self.top = None
        # self.head = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top is None:
            self.top = node
            # self.head = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        # elif self.top == self.head:
        #     self.top = None
        #     self.head = None
        #     self.size = 0
        else:
            popped_value = self.top.data
            self.top = self.top.next
            return popped_value
        self.size -= 1

    def top_value(self):
        return self.top.value

    def S_size(self):
        return self.size

    def __str__(self):
        data = "["
        i = self.top
        while i is not None:
            data += str(i.value)
            data += ", "
            i = i.next
        data += "]"
        return data












