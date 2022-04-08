import sys#we use sys to assign the infinite cost to all the element 
from heapq import heapify, heappush, heappop#heapq library to help us use heap function

def djikstra(graph,src,dest):
    inf = sys.maxsize#max size will return the infinite valute we can hold or the max value
    node_data={'A':{'cost':inf,'pred':[]},#this is the dictionary in dictionary, so every node will have the cost and predesesor same as explanation in Word
    #pred will give the node after the parent node
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]}
    }
    #we should assign the cost to zero right to start the algorithm
    node_data[src]['cost']=0
    visited=[]#initialize the visited element 
    temp=src#it will reassigning for every source variable to the elemetn which is minimum out of all neighbor
    for i in range(5): #5 from the N-1 vertices in word
        if temp not in visited : #check whether temp is in vsiited
            visited.append(temp)#if not then append it to the list visited
            min_heap=[]
            for j in graph[temp]:#this loop use to traverse inside to the neighbor of this temp, so the temp is A and to find the neighbor of A
                #the point it will run in the dictionary of dictionary
                if j not in visited:
                    cost=node_data[temp]['cost']+graph[temp][j]#temp is the current visited nde and cost will see the value inside
                    #and the graph is the value from the temp, so if the temp is A then the value will be 4 and 5 
                    if cost < node_data [j]['cost']:#this for comparison to see if the smallest then ...
                        node_data[j]['cost']=cost#this will be assign the cost for the node_data so the B will be 4 and the C will be 5
                        node_data[j]['pred']=node_data[temp]['pred'] + list(temp) #we will assign the predesesor from the node we are already visiting, so A will be predesesor of B
                    heappush(min_heap,(node_data[j]['cost'],j))# so this is for push to the min heap, so the point i append the cost of B and C to the min_heap
        heapify(min_heap)#is going to create min_heap
        temp=min_heap[0][1]#1 is the second variable.[0 is the minimum elemen of mean heap]so 0 is cost but we want to reassign the cost so tje 1 is the j, the point this statment is will assign the value of temp equals to B so 0 is minimum element and 1 is represent the element which is j
    print("Shortest Distance : "+str(node_data[dest]['cost']))#printing the shortest distance, and the distance will be teh cost from destination position
    print("Shortest Path : "+str(node_data[dest]['pred']+list(dest)))#bassicaly the shortest path from the A



if __name__=="__main__":
    graph={
        'A':{'B':4,'C':5},
        'B':{'A':4,'C':11,'D':9,'E':7},
        'C':{'A':5,'B':11,'E':3},
        'D':{'B':9,'E':13,'F':2},
        'E':{'B':7,'C':3,'D':13,'F':6},
        'F':{'D':2,'E':6}
    }

    source='A'
    destination ='F'
    djikstra(graph,source,destination)