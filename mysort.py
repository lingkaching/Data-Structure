#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:47:16 2017

@author: KACHING
"""
import numpy as np

def BubbleSort(Array):
    n=len(Array)
    for i in range(0,n-1):
       for j in range(0,n-1-i):
           if Array[j]>Array[j+1]:
               Array[j],Array[j+1]=Array[j+1],Array[j]                  
    return Array
    
def SelectSort(Array):
    n=len(Array)
    for i in range(0,n-1):
        MinIndex=i
        for j in range(i+1,n):
            if Array[j]<Array[MinIndex]:
                MinIndex=j
            if i!=MinIndex:
                Array[i],Array[MinIndex]=Array[MinIndex],Array[i]        
    return Array
    
def InsertionSort(Array):
    n=len(Array)
    for i in range(1,n):
        tmp=Array[i]
        j=i
        while Array[j-1]>tmp and j>0:
            Array[j]=Array[j-1]
            j-=1
        Array[j]=tmp
    return Array
    
def QuickSort(Array):
    n=len(Array)
    QSort(Array,0,n-1)
    return Array
    
def QSort(Array,left,right):
    if left<right:        
        i=RandomisedPartition(Array,left,right)
        QSort(Array,left,i-1)
        QSort(Array,i+1,right)
        
def RandomisedPartition(Array,left,right):
    p=np.random.randint(left,right)
    Array[p],Array[right]=Array[right],Array[p]
    pivot=Array[right]
    j=left-1
    for i in range(left,right-1):
        if Array[i]<pivot:
            j+=1
            Array[j],Array[i]=Array[i],Array[j]
    Array[j+1],Array[right]=Array[right],Array[j+1]
    return j+1
#Merge sort version1 based on C language            
def MergeSort1(Array):
    n=len(Array)
    Tmp=[None]*n
    MSort(Array,Tmp,0,n-1)    
    return Array

def MSort(Array,Tmp,left,right):
    if left<right:
        center=int(np.floor((left+right)/2))
        MSort(Array,Tmp,left,center)
        MSort(Array,Tmp,center+1,right)
        Merger(Array,Tmp,left,center,right)
    
def Merger(Array,Tmp,left,center,right):
    i=left
    j=center+1
    k=left
    num_elements=right-left+1
    while i<=center and j<=right:
        if Array[i]<Array[j]:
            Tmp[k]=Array[i]
            i+=1
            k+=1
        else:
            Tmp[k]=Array[j]
            j+=1  
            k+=1 
    while i<=center:
        Tmp[k]=Array[i]
        i+=1
        k+=1
    while j<=right:
        Tmp[k]=Array[j]
        j+=1  
        k+=1         
    for n in range(0,num_elements):
        Array[right]=Tmp[right]
        right-=1
#Merge sort version2 based on Python
def MergeSort2(Array):
    n=len(Array)
    if n<=1:
        return Array
    center=int(np.floor(n/2))
    left=MergeSort2(Array[:center])
    right=MergeSort2(Array[center:])      
    return Merge2(left,right)

def Merge2(left,right):
    tmp=[]
    m=len(left)
    n=len(right)
    i,j=0,0
    while i<m and j<n:
        if left[i]<right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1
    while i<m:
        tmp.append(left[i])
        i+=1
    while j<n:   
        tmp.append(right[j])
        j+=1
    return tmp

def HeapSort(Array):
#build heap 
    n=len(Array)
    m=int(n/2)
    for i in range(m-1,-1,-1):
        Percdown(Array,i,n)
#take the maximum num and maintain the heap    
    for i in range(n-1,0,-1):
        Array[0],Array[i]=Array[i],Array[0]
        Percdown(Array,0,i)
    return Array   

def Percdown(Array,i,N):
    tmp=Array[i]
    while 2*i+1<N:
        child=2*i+1
        if child!=N-1 and Array[child+1]>Array[child]:
            child+=1
        if Array[child]>tmp:
            Array[i]=Array[child]
        else:
            break
        i=child
    Array[i]=tmp

def ShellSort(Array):
    n=len(Array)
    increment=int(np.floor(n/2))
    while  increment>0:    
        j=0
        while j<increment:            
            for k in range(j+increment,n,increment):                
                tmp=Array[k]
                i=k-increment
                while Array[i]>tmp and i>=0:
                    Array[i+increment]=Array[i]
                    i-=increment
                Array[i+increment]=tmp
            j+=1
        increment=int(np.floor(increment/2))
    return Array




           
    
    
    
def main():
    TestArray=[10,23,1,53,654,54,16,646,65,3155,546,31]
#==============================================================================
#     print('Bubble Sort:')   
#     print(BubbleSort(TestArray))
#     print('Select Sort:')
#     print(SelectSort(TestArray))
#     print('Insertion Sort:')
#     print(InsertionSort(TestArray))
#     print('Quick Sort:')
#     print(QuickSort(TestArray))
#==============================================================================
#==============================================================================
#     print('Merge Sort 1:')
#     print(MergeSort1(TestArray))   
#     print('Merge Sort 2:')
#     print(MergeSort2(TestArray))
#==============================================================================
#==============================================================================
#     print('Heap Sort:'):
#     print(HeapSort(TestArray))
#==============================================================================
    print('Shell Sort:')
    print(ShellSort(TestArray))
    
       
if __name__=='__main__':
    main()
    