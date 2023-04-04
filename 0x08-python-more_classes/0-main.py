#!/usr/bin/python3
# Import the Rectangle class from 0-rectangle.py
Rectangle = __import__('0-rectangle').Rectangle

# Create a new Rectangle object and print its type and attributes
rect = Rectangle()
print(type(rect))
print(rect.__dict__)
