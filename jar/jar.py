import sys
class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):

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
        if size>12:
            sys.exit("Invalid")
        self._size=size
jar=Jar()
jar.deposit(1)
print(jar)

