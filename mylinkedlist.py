#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:13:29 2017

@author: KACHING
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import pdb


class Node:
    def __init__(self, element, next=None):
        self.element=element
        self.next=next

class LinkedList:
#LinkedList methods
#Create an empty LinkedList 
    def __init__(self):	
        self.head=None
		
	
#Return True if the linked list is empty
    def IsEmpty(self):
        return self.head==None
  
#Delete the linked list
    def DeleteList(self):
        self.head=None
 	
#Insert an element at the head of a singly linked list
    def InsertHead(self, element):
        p=Node(element)
        if self.IsEmpty():
            self.head=p
        else:
            p.next=self.head
            self.head=p
    
#Find an element x in the linked list
    def Find(self,x):
        p=self.head
        position=1
        while p!=None and p.element!=x:
            p=p.next
            position+=1
        if p==None:
            print('%s is not in the list.' % x )
            return None
        else:
            print('%s is No.%d element.' % (x,position))
            return position
 
#Delete an element x in the linked if existed
    def Delete(self, x):
        p=self.head
        q=p.next
        if self.IsEmpty():
            print('the linked list is empty.')
        elif p.element==x:
            self.head=q
        else:
            while q!=None and q.element!=x:
                p=q
                q=q.next   
            if q==None:
                print('%s is not in the list.' % x )
            else:    
                p.next=q.next
                print('%s is deleted successfully.' % x )
                self.DisplayList()
#Reverse the linked list in place
    def Reverse(self):
        if self.IsEmpty():
            print('the linked list is empty.')    
        else:    
            p=self.head
            q=p.next
            p.next=None
            while q!=None:
                r=q.next
                q.next=p
                p=q
                q=r
            self.head=p
            self.DisplayList()	 
#Display all elements in the linked list
    def DisplayList(self):
        if self.IsEmpty():
            print('the linked list is empty')
        p=self.head
        while p != None:
            print('=>%s' % p.element)
            p=p.next


            
            
if __name__=='__main__':
    L=LinkedList()
    L.InsertHead(2)
    L.InsertHead(7)
    L.InsertHead(5)
    L.InsertHead(10)
    L.DisplayList()
    L.Find(5)
    L.Find(8)
    L.Delete(5)
    L.Delete(11)
    L.Reverse()
    
    

