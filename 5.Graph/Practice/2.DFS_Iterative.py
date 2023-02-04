from collections import deque

def DFSIterative(adj_list, visited, node):
    stack = deque()
    stack.append(node)
    visited.add(node)
    
    while stack:
        v = stack.pop()
        print(v,end=" ")
        for neighbour in reversed(adj_list[v]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

if __name__ == "__main__":
    adj_list = {
        "A": ["B", "C", "D"],
        "B": ["E"],
        "C": ["D", "E"],
        "D": [],
        "E": []
    }
    visited = set()

    for node in adj_list.keys():
        if node not in visited:
            DFSIterative(adj_list, visited, node)