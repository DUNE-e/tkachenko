def dfs(graph, start, end=None):
    visited = set()
    stack = [(start, 0)]  # (vertex, distance)
    traversal_order = []
    path_length = None
    
    while stack:
        vertex, distance = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            
            # Если достигли конечной вершины
            if end is not None and vertex == end:
                path_length = distance
                break
                
            # Добавляем соседей
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append((neighbor, distance + 1))
    
    if end is None:
        return traversal_order
    else:
        return path_length if path_length is not None else -1

# Пример использования
if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = build_graph(edges)
    
    # Пример 1: только обход
    print("DFS traversal from 1:", dfs(graph, 1))
    
    # Пример 2: длина пути
    a, b = 2, 4
    length = dfs(graph, a, b)
    print(f"Path length from {a} to {b}: {length}") 