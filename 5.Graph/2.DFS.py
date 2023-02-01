# graph representation
adj_list = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["D", "E"],
    "D": [],
    "E": []
}

visited = set()
parent = {node:None for node in adj_list.keys()}
dfs_traversal_output = []

def DFS(visited, adj_list, root):
    dfs_traversal_output.append(root)
    visited.add(root)
    for neighbour in adj_list[root]:
        if neighbour not in visited:
            parent[neighbour] = root
            DFS(visited, adj_list, neighbour)
    

for node in adj_list:
    if node not in visited:
        DFS(visited, adj_list, node)

print(dfs_traversal_output)