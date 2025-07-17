class Student:
    def __init__(self, id = 0, name = '', marks = 0.0):
        self.id = id
        self.name = name
        self.marks = marks
    
class Node:
    def __init__(self, student = None):
        self.data = student
        self.link = None

    def create_student(self):
        id = int(input("Enter student ID:"))
        name = input("Enter student name:")
        marks = float(input("Enter student marks"))
        student = Student(id, name, marks)
        self.data = student
    
class Queue:
    def __init__(self):
        self.front = None

    def insert(self):
        node = Node()
        student = node.create_student()
        if self.front == None:
            self.front = node
        return