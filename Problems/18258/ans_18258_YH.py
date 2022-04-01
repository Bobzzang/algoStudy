#https://www.acmicpc.net/problem/18258
#https://one-step-a-day.tistory.com/112

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.qsize = 0
    
    def enqueue(self,data):
        NewNode = Node(data)
        if self.head.data is None:
            self.head = NewNode
            self.tail = NewNode
            self.head.next = self.tail
        else:
            self.tail.next = NewNode 
            self.tail = NewNode
        self.qsize+=1        

    def dequeue(self):
        if self.isempty():
            self.head = Node(None)
            self.tail = Node(None)
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.qsize-=1
            return data

    def isempty(self):
        if self.qsize:
            return 0
        return 1

    def front(self):
        if self.qsize:
            return self.head.data
        return -1
    
    def back(self):
        if self.qsize:
            return self.tail.data
        return -1
    
    def size(self):
        return self.qsize


def solve():
    input = sys.stdin.readline
    N = int(input())
    queue = Queue()
    for _ in range(N):
        cmd = input().strip()
        if cmd == "pop":
            print(queue.dequeue())
        elif cmd == "size":
            print(queue.size())
        elif cmd == "empty":
            print(queue.isempty())
        elif cmd == "front":
            print(queue.front())
        elif cmd == "back":
            print(queue.back())
        else :
            _, num = cmd.split()
            queue.enqueue(int(num))
    return

if __name__ == "__main__":
    solve()