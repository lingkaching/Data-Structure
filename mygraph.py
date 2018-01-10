#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:33:27 2017

@author: KACHING
"""

from myqueue import Queue
from mypriorityqueue1 import PriorityQueue
import numpy as np
import pdb

class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        
    def addNeighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices+=1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        
    def getVertex(self,v):
        if v in self.vertList:
            return self.vertList[v]
        else:
            return None
    def getVertices(self):
        return self.vertList.values()
    def addEdge(self,m,n,weight=0):
        if m not in self.vertList:
            self.addVertex[m]
        if n not in self.vertList:
            self.addVertex[n]
        self.vertList[m].addNeighbour(self.vertList[n],weight)
        
def InitGraph():
    G=Graph()
    for v in ['s','t','x','y','z']:
        G.addVertex(v)
    G.addEdge('s','t',10)
    G.addEdge('s','y',5)
    G.addEdge('t','y',2)
    G.addEdge('t','x',1)
    G.addEdge('x','z',4)
    G.addEdge('y','t',3)
    G.addEdge('y','x',9)    
    G.addEdge('y','z',2)
    G.addEdge('z','x',6)
    G.addEdge('z','s',7)
    
      
#==============================================================================
#     for v in G.vertList.values():
#         for w in v.getConnections():
#             print("( %s , %s , %s )" % (v.getId(), w.getId(), v.getWeight(w)))
#==============================================================================
    return G

def BFS(G,s):
    for u in G.getVertices():
        if u!=s:
            u.color='white'
            u.d=np.inf
            u.pre=None
    s.color='gray'
    s.d=0
    s.pre=None
    Q=Queue()
    Q.Enqueue(s)
    while not Q.IsEmpty():
        u=Q.Dequeue()
        for v in u.getConnections():
            if v.color=='white':
                v.color='gray'
                v.d=u.d+1
                v.pre=u
                Q.Enqueue(v)
        u.color='black'

def PrintPath(G,s,v):
    if v==s:
        print(s.getId())
    elif v.pre==None:
        print('no path from %s to %s' % (s.getId(),v.getId()))
    else:
        PrintPath(G,s,v.pre)         
        print(v.getId())
 
def DFS(G):
    for u in G.getVertices(): 
        u.color='white'
        u.pre=None
    for u in G.getVertices():
        if u.color=='white':
            DFS_VISIT(G,u)

def DFS_VISIT(G,u):
    global time
    time+=1
    u.d=time
    u.color='gray'
    for v in u.getConnections():
        if v.color=='white':
            v.pre=u
            DFS_VISIT(G,v)
    u.color='black'
    time+=1
    u.f=time
    print('%s %s' % (u.f,u.getId()))
    
def Dijkstra(G,s):
    InitialiseSingleSource(G,s)
    S=[]
    PQ=PriorityQueue()
    items=[ (v.d, v) for v in G.getVertices()]
    PQ.BuildHeap(items)
    
    while not PQ.IsEmpty():
        u=PQ.DeleteMin()[1]
        S.append(u)
        for v in u.getConnections():
            Relax(u,v,u.getWeight(v))
    
def InitialiseSingleSource(G,s):
    for v in G.getVertices():                
        v.d=np.inf
        v.pre=None
    s.d=0  

def Relax(u,v,w_uv):
    if v.d>u.d+w_uv:
        v.d=u.d+w_uv
        v.pre=u
        
    
    
    
def main():
    G=InitGraph()
    
#==============================================================================
#     BFS(G,G.getVertex('s'))
#     PrintPath(G,G.getVertex('s'),G.getVertex('y'))
#==============================================================================
    
#==============================================================================
#     DFS(G)
#==============================================================================
    Dijkstra(G,G.getVertex('s'))
    PrintPath(G,G.getVertex('s'),G.getVertex('z'))
    

    
if __name__=='__main__':
    time=0
    main()
    



