from collections import deque

def BFSRecursive(adj_list, visited, queue):
    # base condition
    if not queue:
        return
        
    # print the visited node
    v = queue.popleft()
    print(v, end=' ')

    # check all the neighbours of the visited node
    for neighbour in adj_list[v]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    
    BFSRecursive(adj_list, visited, queue)


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
    queue = deque()

    for node in adj_list.keys():
        if node not in visited:
            queue.append(node)
            visited.add(node)
            BFSRecursive(adj_list, visited, queue)

