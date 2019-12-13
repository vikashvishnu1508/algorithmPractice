# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        self.head = node

    def setTail(self, node):
        # Write your code here.
        self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        nodeToInsert.next = node
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        node.next = nodeToInsert
        nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(7)


headSet = DoublyLinkedList()
headSet.setHead(first)
headSet.setTail(fifth)

headSet.insertAfter(first, second)
print(first.next.value)
print(second.prev.value)
headSet.insertAfter(second, third)
print(second.next.value)
print(third.prev.value)
headSet.insertAfter(third, fourth)
print(third.next.value)
print(fourth.prev.value)
headSet.insertAfter(fourth, fifth)
print(fourth.next.value)
print(fifth.prev.value)

print(headSet.head.value)
print(headSet.tail.value)

print("insert before")
headSet.insertBefore(sixth, fourth)
print(first.next.value)
print(second.next.value)
print(third.next.value)
print(fourth.next.value)
print(fifth.next.value)
print(sixth.next.value)


print("reverse")
print(first.next.value)
print(second.prev.value)
print(third.prev.value)
print(fourth.prev.value)
print(fifth.prev.value)
print(sixth.prev.value)