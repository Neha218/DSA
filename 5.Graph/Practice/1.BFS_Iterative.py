from collections import deque

def BFSIterative(adj_list, visited, node):
    queue = deque()
    queue.append(node)
    visited.add(node)

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for neighbour in adj_list[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    adj_list = {
        "A":["B","D"],
        "B":["A","C"],
        "C":["B"],
        "D":["A","E","F"],
        "E":["D","F","G"],
        "F":["D","E", "H"],
        "G":["E","H"],
        "H":["G","F"],
    }

    visited = set()

    for node in adj_list.keys():
        if node not in visited:
            BFSIterative(adj_list, visited, node)