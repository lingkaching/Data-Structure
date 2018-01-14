#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:56:14 2018

@author: KACHING
"""
import numpy as np

def isoperand(c):
    # c is a char
    if ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z'):
        return True
def precedence(o):
    # o is an operator
    if o=='+' or o=='-':
        return 1
    elif o=='*' or o=='/':
        return 2
    elif o=='^':
        return 3
    else:
        return -1
    
def infixtopostfix(exp):
    #exp is an expression
    n=len(exp)
    re=[]
    Stack=[]
    for i in range(0,n):
        if isoperand(exp[i]):
            re.append(exp[i])
        elif exp[i]=='(':
            Stack.append(exp[i])
        elif exp[i]==')':
            while Stack[-1]!='(':
                tmp=Stack.pop()
                re.append(tmp)
            Stack.pop()
        else:            
            while len(Stack)!=0 and precedence(Stack[-1])>=precedence(exp[i]):
                tmp=Stack.pop()
                re.append(tmp)
            Stack.append(exp[i])  
    while len(Stack)!=0:
        tmp=Stack.pop()
        re.append(tmp)
    return ''.join(re)

def ismatchingpair(char1,char2):
    if char1=='(' and char2==')':
        return True
    elif char1=='[' and char2==']':
        return True
    elif char1=='{' and char2=='}':
        return True
    else:
        return False
        
def areParenthesisBalanced(exp):
    n=len(exp)
    Stack=[]
    for i in range(0,n):
        if exp[i] in ['(','[','{']:
            Stack.append(exp[i])
        if exp[i] in [')',']','}']:
            if len(Stack)==0:
                return False
            tmp=Stack.pop()
            if not ismatchingpair(tmp,exp[i]):
                return False
    return True if len(Stack)==0 else False
        
def towerofhanoi1(n,from_rod,to_rod,aux_rod):
    if n==1:
        print('Move disk %s from %s to %s' % (n,from_rod,to_rod))
        return
    towerofhanoi(n-1,from_rod,aux_rod,to_rod)
    print('Move disk %s from %s to %s' % (n,from_rod,to_rod))
    towerofhanoi(n-1,aux_rod,to_rod,from_rod)
def towerofhanoi2(n):
    A=[np.inf]+list(range(n,0,-1))
    B=[np.inf]
    C=[np.inf]
    nums=2**n-1
    for i in range(1,nums+1):
        if i%3==1:
            MoveDisk(A,C,1)
        elif i%3==2:
            MoveDisk(A,B,2)
        else:
            MoveDisk(B,C,0)            

def MoveDisk(rod1,rod2,flag):
    tmp1=rod1.pop()
    tmp2=rod2.pop()
    if tmp1<tmp2:
        rod2.append(tmp2)
        rod2.append(tmp1)
        if flag==1:
            print('Move disk %s from A to C' % tmp1)
        elif flag==2:
            print('Move disk %s from A to B' % tmp1)
        else:
            print('Move disk %s from B to C' % tmp1)
    else:
        rod1.append(tmp1)
        rod1.append(tmp2)
        if flag==1:
            print('Move disk %s from C to A' % tmp2)
        elif flag==2:
            print('Move disk %s from B to A' % tmp2)
        else:
            print('Move disk %s from C to B' % tmp2)

def main():
#==============================================================================
#     exp='a+b*(c^d-e)^(f+g*h)-i'
#     exp1='{()}[]]'
#     print(infixtopostfix(exp))
#     print(areParenthesisBalanced(exp1))
#==============================================================================
    towerofhanoi1(3,'A','B','C')
    print()
    towerofhanoi2(2)
    
if __name__=='__main__':
    main()