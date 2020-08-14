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
        temp = self.head  
        if temp is not None:  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
        temp = None
        
    def deleteNthNode(self, pos):
        if self.head is None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(pos-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return 
        if temp.next is None:
            return
        n = temp.next.next
        temp.next = None
        temp.next = n
        
    def deleteNthFromEnd(self, pos):
        temp = self.head
        if temp is None:
            return
        l = 0
        while temp is not None:
            l += 1
            temp = temp.next
        c = l - pos
        if c < 0:
            return
        temp = self.head
        if c == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(c-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        x = temp.next.next
        temp.next = None
        temp.next = x
        
    def reverseLinkedList(self):
        prev = None
        current = self.head
        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
    def searchEle(self, ele):
        current = self.head
        while (current):
            if current.data == ele:
                print("Element Present")
                return True
            current = current.next
        print("element Not Present")
        return False
    
    def palindrome(self):
        small = self.head
        big = self.head
        while(1):
            big = big.next
            if big.next is None:
                second = small.next.next
                break
            if big is None:
                second = small.next
                break
            small = small.next
        small.next = None
        small = self.head
        while small is not None:
            print(small.data, end = " ")
            small = small.next
        print()
        while second is not None:
            print(second.data, end = " ")
            second = second.next
        print()
            
            
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
ll.push(10)
ll.printList()
ll.insertAfter(ll.head.next, 3)
ll.printList()
ll.append(9)
ll.printList()
ll.searchEle(9)
print(ll.NthNode(4))
print(ll.NthFromEnd(2))
ll.printList()
print("-----------")
ll.palindrome()
print("-----------")
ll.printList()
ll.deleteNode(100)
ll.printList()
ll.deleteNthNode(2)
ll.printList()
ll.deleteNthFromEnd(4)
ll.printList()
ll.reverseLinkedList()
ll.printList()
ll.palindrome()












