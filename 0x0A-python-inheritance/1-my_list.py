#!/usr/bin/python3

class MyList:
    def __init__(self):
        self.list = []

    def append(self, value):
        self.list.append(value)

    def print_sorted(self):
        self.list.sort()
        print(self.list)

    def __str__(self):
        return str(self.list)
