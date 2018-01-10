#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:54:36 2017

@author: KACHING
"""
#PriorityQueue for Graph 
class PriorityQueue:
    def __init__(self):
        self.items=[]
        self.size=0
    def IsEmpty(self):
        return self.size==0
    def BuildHeap(self,items):  
        self.items=items
        self.size=len(self.items)
        i=self.size//2-1
        for j in range(i,-1,-1):
            self.Percdown(j,self.size)
    def Percdown(self,i,n):
        tmp=self.items[i]
        child=2*i+1
        while child<n:
            if child!=n-1 and self.items[child+1][0]<self.items[child][0]:
                child+=1
            if self.items[child][0]<tmp[0]:
                self.items[i]=self.items[child]
            else:
                break
            i=child
            child=2*i+1
        self.items[i]=tmp      
    def DeleteMin(self):
        if self.size==1:
            Min=self.items.pop()
            self.size-=1
        else:
            self.items[0],self.items[-1]=self.items[-1],self.items[0]
            Min=self.items.pop()
            self.size-=1
            self.Percdown(0,self.size)
        return Min
    def Insert(self,element):
        self.items.append(element)
        self.size+=1
        self.Percup(self.size)
    def Percup(self,n):
        i=n-1
        parent=n//2-1
        tmp=self.items[i]
        while i>=0:
            if self.items[parent][0]>tmp[0]:
                self.items[i]=self.items[parent]
            else:
                break
            i=parent
            parent=(i+1)//2-1
        self.items[i]=tmp

if __name__=='__main__':
    test=[(33,'a'), (27,'b'),(21,'c'), (19,'d')]
    PQ=PriorityQueue()
    PQ.BuildHeap([ x for x in test])
    
    print(PQ.items)
    PQ.Insert((7,'e'))
    for i in range(0,5):
         a=PQ.DeleteMin()
    print(PQ.items)
    
    
        
        
    
        
        
        
        
        
        