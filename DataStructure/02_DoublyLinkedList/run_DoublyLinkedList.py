from doublyLinkedList import DoublyLinkedList

l = DoublyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)

print(l.next())
print(l.next())
print(l.before())
print(l.next())
print(l.next())
print(l.popFirst())
print(l.popLast())

print("========")

print(l.next())
print(l.next())
print(l.next())
l.insert(10)
print(l.before())
print(l.before())
l.insert(11)
print(l.next())
l.insert(12)

print("========")
print(l.first())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())