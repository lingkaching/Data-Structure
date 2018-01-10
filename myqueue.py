#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:11:50 2017

@author: KACHING
"""

class Queue:
    def __init__(self):
        self.items=[]
    def IsEmpty(self):
        return len(self.items)==0
    def Enqueue(self,element):
        self.items.insert(0,element)
    def Dequeue(self):
        return self.items.pop()
        
if __name__=='__main__':
    x=Queue()
    x.Enqueue(1)
    x.Enqueue(2)
