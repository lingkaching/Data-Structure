#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:18:03 2017

@author: KACHING
"""

class TreeNode:
    def __init__(self, element, left=None, right=None):
        self.element=element
        self.left=left
        self.right=right
        
class BinarySearchTree:
#initialise the BST    
    def __init__(self):
        self.root=None
        
#make empty
    def MakeEmpty(self):
        self.root=None

#Find the minimum number in the tree(recursion)
    def FindMin(self):
        return self.FindMin_BST(self.root)
    def FindMin_BST(self, T):
        if T==None:
            return None
        elif T.left==None:
            return T
        else:
            return self.FindMin_BST(T.left)
            
#Find the maximum number in the tree(non-recursion)
    def FindMax(self):
        T=self.root
        if T==None:
            return None
        else:
            while T.right!=None:
                T=T.right
            return T
 
#Find element x
    def Find(self, x):
        return self.Find_BST(x, self.root)
    def Find_BST(self, x, T):  
        if T==None:
            return None
        elif x<T.element:
            return self.Find_BST(x, T.left)
        elif x>T.element:
            return self.Find_BST(x, T.right)
        else:
            return T
            
#Insert element
    def Insert(self, x): 
        T=self.root
        self.root=self.Insert_BST(T, x)
    def Insert_BST(self, T, x):
        if T==None:
            T=TreeNode(x)                   
        elif x<T.element:
             T.left=self.Insert_BST(T.left, x)
        elif x>T.element:
             T.right=self.Insert_BST(T.right, x)
        else:
            print('%s is already in the Tree.' % x)
        return T
 
#Delete element x in the Tree
    def Delete(self, x):
        self.root=self.Delete_BST(x, self.root)
    def Delete_BST(self, x, T):
        if T==None:
            print('%s is not found in the Tree.' % x)
        elif x<T.element:
            T.left=self.Delete_BST(x, T.left)
        elif x>T.element:
            T.right=self.Delete_BST(x, T.right)
        #element is found
        else: 
            if T.left==None:
                T=T.right
            elif T.right==None:
                T=T.left
            else:        
                Tmpcell=self.FindMin_BST(T.right)
                T.element=Tmpcell.element
                T.right=self.Delete_BST(T.element, T.right)    
        return T

#In order traverse         
    def InOrderTraverse(self):
        
        self.InOrderTraverse_BST(self.root)     
    def  InOrderTraverse_BST(self, T):      
        if T!=None:
           self.InOrderTraverse_BST(T.left)
           print(T.element)
           self.InOrderTraverse_BST(T.right)
           
#Pre order traverse         
    def PreOrderTraverse(self):
        
        self.PreOrderTraverse_BST(self.root)     
    def  PreOrderTraverse_BST(self, T):      
        if T!=None:
           print(T.element)
           self.PreOrderTraverse_BST(T.left)
           self.PreOrderTraverse_BST(T.right)           
            
#Post order traverse         
    def PostOrderTraverse(self):
        
        self.PostOrderTraverse_BST(self.root)     
    def  PostOrderTraverse_BST(self, T):      
        if T!=None:           
           self.PostOrderTraverse_BST(T.left)
           self.PostOrderTraverse_BST(T.right)   
           print(T.element)
           
if __name__=='__main__':
    
    T=BinarySearchTree()
    T.Insert(8)
    T.Insert(3)
    T.Insert(10) 
    T.Insert(1) 
    T.Insert(6) 
    T.Insert(14) 
    T.Insert(4) 
    T.Insert(7)
    T.Insert(13) 
    T.InOrderTraverse() 
    print('---')
    T.PreOrderTraverse()  
    print('---')
    T.PostOrderTraverse()
    print('---')
    print(T.FindMin().element)
    print(T.FindMax().element) 
    print('---')
    T.Delete(8)  
    T.InOrderTraverse() 
    print('---')
    T.Delete(20)
    
    