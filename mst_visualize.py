import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal(num_vertices, edges):
    uf = UnionFind(num_vertices)
    mst = []
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    return mst

def prim(num_vertices, edges):
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    mst = []
    visited = [False] * num_vertices
    min_heap = [(0, 0)]  # Start with vertex 0
    prev = None

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if prev is not None:
            mst.append((prev, u, weight))
        prev = u
        for edge_weight, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v))

    return mst

def visualize_graph(edges, title, mst_edges=None):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='black')

    # Draw edge labels
    edge_labels = {(u, v): weight for u, v, weight in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if mst_edges:
        # Draw MST edges in red
        mst_edges_set = set((min(u, v), max(u, v), weight) for u, v, weight in mst_edges)
        for u, v, weight in edges:
            if (min(u, v), max(u, v), weight) in mst_edges_set:
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='red', width=2)
    
    plt.title(title)
    plt.show()

# Smaller example graph
num_vertices = 5
edges = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 5),
    (4, 0, 6),
    (0, 2, 7),
    (1, 3, 8)
]

# Run Kruskal's Algorithm
try:
    mst_kruskal = kruskal(num_vertices, edges)
    print("Kruskal's MST:", mst_kruskal)
    visualize_graph(edges, "Kruskal's Algorithm MST", mst_edges=[(u, v, weight) for u, v, weight in mst_kruskal])
except ValueError as e:
    print(f"Error in Kruskal's Algorithm: {e}")

# Run Prim's Algorithm
try:
    mst_prim = prim(num_vertices, edges)
    print("Prim's MST:", mst_prim)
    visualize_graph(edges, "Prim's Algorithm MST", mst_edges=[(u, v, weight) for u, v, weight in mst_prim])
except ValueError as e:
    print(f"Error in Prim's Algorithm: {e}")
