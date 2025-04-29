def dfs(graph, start, end=None):
    # Проверка на корректность входных (новый комментарий) данных
    if not graph:
        raise ValueError("Graph cannot be empty")
    if start not in graph:
        raise ValueError(f"Start vertex {start} not found in graph")
    if end is not None and end not in graph:
        raise ValueError(f"End vertex {end} not found in graph")

"""
Comments
Комментарии новые добавленные,,,,,,,
"""

"""
НОВЫЕ КОММЕНТЫ...
"""

    visited = set()
    stack = [(start, 0)]  # (vertex, distance)
    traversal_order = []
    path_length = None
    
    while stack:
        vertex, distance = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            
            if end is not None and vertex == end:
                path_length = distance
                break
                
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append((neighbor, distance + 1))
    
    if end is None:
        return traversal_order
    else:
        return path_length if path_length is not None else -1
