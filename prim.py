import heapq
from collections import defaultdict

def prim(num_vertices, edges):
    graph = defaultdict(list)
    for u, v, weight in edges:
        if u >= num_vertices or v >= num_vertices:
            raise ValueError(f"Edge ({u}, {v}) references an invalid vertex index")
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

if __name__ == "__main__":
    num_vertices = 100
    # Ensure that indices are within the range [0, num_vertices-1]
    edges = [(i % num_vertices, (i + 1) % num_vertices, (i % 10) + 1) for i in range(300)]  # Fixed edges

    try:
        mst_prim = prim(num_vertices, edges)
        print("Prim's MST:", mst_prim)
    except ValueError as e:
        print(f"Error in Prim's Algorithm: {e}")
