#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:44:39 2018

@author: KACHING
"""

class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.root=None
    
    def isEmpty(self):
        return True if not self.root else False
        
    def push(self,data):
        NewNode=StackNode(data)
        NewNode.next=self.root
        self.root=NewNode        
    def pop(self):
        if self.isEmpty():
            print('Stack is empty!')
            return
        else:
            tmp=self.root
            self.root=tmp.next
            return tmp.data
    def top(self):
        if self.isEmpty():
            print('Stack is empty!')
            return
        else:
            return self.root.data

def main():
    stack=Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    

if __name__=='__main__':
    main()