def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            # Добавляем соседей в обратном порядке для сохранения порядка обхода
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return traversal_order

def build_graph(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Пример использования
if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    start = 1
    graph = build_graph(edges)
    print("DFS traversal:", dfs(graph, start))