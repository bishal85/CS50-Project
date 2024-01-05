import sys
class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size+n>self.capacity:
            sys.exit("Invalid")

        self.size=self.size+n

    def withdraw(self, n):
        self.size=self.size-n


    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self,capacity):
        self._capacity=capacity


    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if self.size>self.capacity:
            sys.exit("Invalid")
        self._size=size
