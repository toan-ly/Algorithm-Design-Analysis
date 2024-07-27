from collections import defaultdict

# Define the graph using an adjacency list
graph = defaultdict(list)

# Add edges based on the provided graph
edges = [
    ("Intro to Programming", "Advanced Programming"),
    ("Advanced Programming", "Intro to Computer Systems"),
    ("Advanced Programming", "Web Programming"),
    ("Advanced Programming", "Software Engineering"),
    ("Advanced Programming", "Databases"),
    ("Databases", "Software Engineering"),
    ("Software Engineering", "Final Project"),
    ("Intro to Computer Systems", "Compiler Theory"),
    ("Intro to Computer Systems", "Programming Languages"),
    ("Intro to Computer Systems", "Operating Systems"),
    ("Intro to Computer Systems", "Computer Architecture"),
    ("Discrete Mathematics", "Data Structures"),
    ("Discrete Mathematics", "Logic"),
    ("Calculus 1", "Discrete Mathematics"),
    ("Calculus 1", "Linear Algebra"),
    ("Calculus 1", "Theory of Computation"),
    ("Linear Algebra", "Artificial Intelligence"),
    ("Data Structures", "Computer Architecture"),
    ("Data Structures", "Databases"),
    ("Data Structures", "Theory of Computation"),
    ("Data Structures", "Algorithms"),
    ("Logic", "Artificial Intelligence"),
    ("Algorithms", "Final Project"),
    ("Algorithms", "Artificial Intelligence"),
]

# Populate the graph
for u, v in edges:
    graph[u].append(v)

# Include nodes with no outgoing edges
all_nodes = set(graph.keys())
for v in graph.values():
    all_nodes.update(v)

# Add nodes with no outgoing edges to the graph
for node in all_nodes:
    if node not in graph:
        graph[node] = []

# Topological Sort using DFS
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
    
    # Perform DFS from each node
    for node in graph:
        if node not in visited:
            dfs(node)
    
    # Return nodes in reverse postorder
    return stack[::-1]

# Test the function
print("Topological Sort order:", topological_sort(graph))