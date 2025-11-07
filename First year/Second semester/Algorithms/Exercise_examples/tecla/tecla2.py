from collections import deque

def bfs(graph, state):
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n  # Per tracciare il percorso
    edges_visited = set()
    
    queue = deque([0])
    visited[0] = True
    state[0] = 'SLURP'  # Stato iniziale del nodo 0
    
    while queue:
        node = queue.popleft()
        
        if node == 0 and state[node] == 'SLURP' and parent[node] != -1:
            path = []
            while node != -1:
                path.append(node)
                node = parent[node]
            path.reverse()
            return len(path) - 1, path
        
        for neighbor in graph[node]:
            edge = (min(node, neighbor), max(node, neighbor))
            if not visited[neighbor] and edge not in edges_visited:
                visited[neighbor] = True
                parent[neighbor] = node
                edges_visited.add(edge)
                state[neighbor] = 'SLURP' if state[node] == 'BLEAH' else 'BLEAH'
                queue.append(neighbor)
    
    return -1, []

def find_path(graph, state):
    return bfs(graph, state)

T = int(input())  # Numero di testcase

for _ in range(T):
    n, m = map(int, input().split())  # Numero di nodi e filamenti
    graph = [[] for _ in range(n)]  # Lista di adiacenza del grafo
    state = ['BLEAH'] * n  # Stato iniziale dello stomaco
    
    for _ in range(m):
        u, v = map(int, input().split())  # Estremità dei filamenti
        graph[u].append(v)
        graph[v].append(u)
    
    steps, path = find_path(graph, state)
    
    # Output
    print(steps)
    if steps != -1:
        print(' '.join(map(str, path)))
    else:
        print(0)
