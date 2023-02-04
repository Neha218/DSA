import sys
from heapq import heapify, heappush, heappop

def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {}
    for node in graph.keys():
        node_data[node] = ({'cost': inf, 'pred': []}) 

    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(len(graph)-1):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for neighbour in graph[temp]:
                if neighbour not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][neighbour]
                    if cost < node_data[neighbour]['cost']:
                        node_data[neighbour]['cost'] = cost
                        node_data[neighbour]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap, (node_data[neighbour]['cost'], neighbour))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: "+str(node_data[dest]['cost']))
    print("Shortest Path: "+str(node_data[dest]['pred'] + list(dest)))

if __name__ == "__main__":
    graph = {
        'A':{'B':2, 'C':4},
        'B':{'A':2, 'C':3,'D':8},
        'C':{'A':4, 'B':3,'E':5,'D':2},
        'D':{'B':8, 'C':2,'E':11,'F':22,},
        'E':{'C':5, 'D':11,'F':1},
        'F':{'D':22, 'E':1},
    }

    source = 'A'
    destination = 'F'
    dijkstra(graph, source, destination)