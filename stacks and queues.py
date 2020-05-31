#Implementation of stack in python:
class Stack:
    def __init__(self):
        self.data = []

    def push(self , value):
        self.data.append (value)

    def pop(self):
        return self.data.pop (-1)

    def top(self):
        return self.data[-1]

    def size(self):
        return len (self.data)

    def is_empty(self):
        return len (self.data) == 0

    def __str__(self):
        return str (self.data)


#Queue implementation in python
class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data)==0

    def size(self):
        return len(self.data)
    def front(self):
        return self.data[0]

    def end(self):
        return self.data[-1]

    def __str__(self):
        return str(self.data)



