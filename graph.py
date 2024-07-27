from collections import deque, defaultdict

graph = {
    1: [2, 3, 7],
    2: [1, 3, 4, 5],
    3: [1, 2, 8],
    4: [2],
    5: [2, 7],
    6: [7],
    7: [1, 5, 6, 8],
    8: [3, 7]
}

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

# Depth-First Search (DFS)
def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):  # reverse for correct order
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

# Test the functions
start_node = 1
print("BFS order:", bfs(graph, start_node))
print("DFS order:", dfs(graph, start_node))
