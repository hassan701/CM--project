import random
from itertools import permutations
import sys
from heapq import heapify, heappush, heappop
import numpy as np
import matplotlib.pyplot as plt
import time as t

#Creating the graph variables

def Graph(n):
    #Determines number of nodes
    numberOfNodes = n
    
    #Used to ensure no duplicate edges
    Edges = {
    
        }
    
    
    #Create tuples for each nodes in dictionary
    for i in range(numberOfNodes):
    
        Edges[i] = []
    
    #Used to make the node list in the form of (node1, node2, distance)
    nodeList = []
    
    
    #Creating the Graph
    graph = [[0 for x in range(numberOfNodes)] for y in range(numberOfNodes)]
    
    #Create links between 2 random nodes
    for i in range(numberOfNodes):
    
        for j in range(numberOfNodes):
          
            weight = random.randint(2, 20)
    
        #Ensures no link to itself and no duplicate links between nodes
            if i != j and i not in Edges[j]:
    
                Edges[i] += (j,)
                Edges[j] += (i,)
                nodeList.append((i, j, weight))
    
    #Plotting the graph
    for nodeA, nodeB, weight in nodeList:
    
        graph[nodeA][nodeB] = weight
        graph[nodeB][nodeA] = weight
        
    return graph



#Brute Force Method

#Used for Permutation in Brute Force
def Brute(graph,n):
    permList = list(permutations([i for i in range(n)]))
    
    bruteForceCost = float("inf")
    path = []
    
    
    for p in permList:
    
            bruteForceCurrentCost = 0
    
            for i in range(n - 1):
            
                bruteForceCurrentCost += graph[p[i]][p[i + 1]]
    
            if bruteForceCurrentCost < bruteForceCost:
    
                bruteForceCost = bruteForceCurrentCost
                path = p
    #print(bruteForceCost)
    #print(path)


def Nearest(graph,n):
#Nearest Neighbor
    
    visitedNodes = [0]
    costToNode = [0]
    
    currentNode = 0
    currentCost = 0
    
    for k in range(n - 1):
        currentShortest = float("inf")
        for s in range(n):
            if s != currentNode and s not in visitedNodes and graph[currentNode][s] < currentShortest:
    
                nextNode = s
                currentShortest = graph[currentNode][s]
                
        visitedNodes.append(nextNode)
        currentNode = nextNode
        currentCost += currentShortest
        costToNode.append(currentCost)
    #print(currentCost)
    #print(visitedNodes)
    #print(costToNode)

def floydWarshall(graph,src,dest, n):
 
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(n):
 
        # pick all vertices as source one by one
        for i in range(n):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(n):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    #print(dist[src][dest])

def dijsktra(graph,src,dest,n):
    #set up our empty matrix 
  inf = sys.maxsize
  node_Data = {}
  for i in range(n):
    node_Data[i] = {'cost':inf, 'pred':[]}
  node_Data[src]['cost'] = 0
  visited = []
  temp = src
  #go through each node
  for i in range(n):
      #check if that node has been visited
    if temp not in visited:
        #add the noted to the visited
      visited.append(temp)
      min_heap = []
      #go to through the nodes attached to the current node
      for j in graph[temp]:
          #check if they have been visted
        if j not in visited:
            #go to that node and the distance to  the total distance
          cost = node_Data[temp]['cost'] + graph[temp][j]
          #check if the new distance is smaller than the current distance of that node
          if cost < node_Data[j]['cost']:
              #update the distance with new smaller distance
            node_Data[j]['cost'] = cost
            node_Data[j]['pred'] = node_Data[j]['pred'] +[temp]
          heappush(min_heap,(node_Data[j]['cost'],j))
    heapify(min_heap)
    if(len(min_heap)!=0):
        #set the new current to the new node
      temp = min_heap[0][1]
    else:
      break
  #print("Shortest Distance: "+ str(node_Data[dest]['cost']))
  #print("Shortest Path: "+ str(node_Data[dest]['pred']+[dest]))

  

def change(graph,n):
    lis = []
    #go through the matrix and reasing it to a new dic 
    for i in range(n):
        a = np.arange(0,n,1)
        dic = dict(zip(a,graph[i]))
        dic.pop(i)
        lis.append(dic)
    a = np.arange(0,n,1)
    data = dict(zip(a,lis))
    return data



nodes = [1,2,3,4,5,6,7,8,9,10]

totalb =[]
totaln =[]
totald =[]
totalf =[]
#loop through all the nodes sizes
for i in nodes:
    t1=0
    t2=0
    t3=0
    t4=0
    for j in range(10):
        graph = Graph(i)
        data = change(graph,i)
        
        startTime = t.time()
        Brute(graph,i)
        endTime = t.time()
        t1+=(endTime-startTime)
        
        startTime = t.time()
        Nearest(graph,i)
        endTime = t.time()
        t2+=(endTime-startTime)
        
        startTime = t.time()
        dijsktra(data,0,i-1,i)
        endTime = t.time()
        t3+=(endTime-startTime)
        
        startTime = t.time()
        floydWarshall(graph,0,i-1,i)
        endTime = t.time()
        t4+=(endTime-startTime)

    #get the avrage runtime from all 10 samples
    totalb.append(t1/10)
    totaln.append(t2/10)
    totald.append(t3/10)
    totalf.append(t4/10)

fig,(ax1, ax2)= plt.subplots(1,2)
ax1.plot(nodes,totalb,linestyle='--', marker='o', label='Brute Force')
ax1.plot(nodes,totaln,linestyle='--', marker='o',color='r', label='Nearest Neighbour')
ax2.plot(nodes,totald, linestyle='--', marker='o', color='g', label='Dijsktra')
ax2.plot(nodes,totalf, linestyle='--', marker='o', color='y', label='floydWarshall')

ax1.set_title("Brute Force v Nearest Neighbour")
ax2.set_title("Dijsktra v floydWarshall")

plt.legend()
plt.show()












