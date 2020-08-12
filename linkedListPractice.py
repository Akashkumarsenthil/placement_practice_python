#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:55:20 2020

@author: akashkumar
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, data):
        if prev_node == None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, data):
        current = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        while current.next:
            current = current.next

        current.next = new_node
        
    def deleteNode(self, key):
        current = self.head
        
        while current is not None:
            if current.data == None:
                break
            prev = current
            current = current.next
        if current == None:
            return 
        prev.next = current.next
        

        
        
    def searchEle(self, ele):
        current = self.head
        while (current):
            if current.data == ele:
                print("Element Present")
                return True
            current = current.next
        print("element Not Present")
        return False
            
            
    def NthNode(self, n):
        current = self.head
        for _ in range(n-1):
            if current is not None:
                current = current.next
        if current == None:
            return "No element in ", n, "th position"
        else:
            return current.data
    def NthFromEnd(self, n):
        current = self.head
        l = 0
        while(current is not None):
            l += 1
            current = current.next
        if n <= l:
            c = l-n
        else:
            return "Enter Valid Number"
        current = self.head
        for _ in range(c):
            current = current.next
        try:
            return current.data
        except:
            return "Enter Valid Number"

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
            return
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
        print()
            
            
ll = LinkedList()
ll.searchEle(9)
ll.printList()
ll.push(5)
ll.push(4)
ll.push(1)
ll.push(100)
ll.printList()
ll.insertAfter(ll.head.next, 3)
ll.printList()
ll.append(9)
ll.printList()
ll.searchEle(9)
print(ll.NthNode(4))
print(ll.NthFromEnd(2))
ll.printList()
ll.deleteNode(1)
ll.printList()












