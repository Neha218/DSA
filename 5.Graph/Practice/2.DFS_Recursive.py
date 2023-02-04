def dfsRecursive(adj_list, visited, node):
    print(node,end=" ")
    for neighbour in adj_list[node]:
         if neighbour not in visited:
            visited.add(neighbour)
            dfsRecursive(adj_list, visited, neighbour)

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
            visited.add(node)
            dfsRecursive(adj_list, visited, node)