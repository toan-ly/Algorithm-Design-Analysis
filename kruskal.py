import heapq

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
        if u >= num_vertices or v >= num_vertices:
            raise ValueError(f"Edge ({u}, {v}) references an invalid vertex index")
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    return mst

if __name__ == "__main__":
    num_vertices = 100
    # Ensure that indices are within the range [0, num_vertices-1]
    edges = [(i % num_vertices, (i + 1) % num_vertices, (i % 10) + 1) for i in range(300)]  # Fixed edges

    try:
        mst_kruskal = kruskal(num_vertices, edges)
        print("Kruskal's MST:", mst_kruskal)
    except ValueError as e:
        print(f"Error in Kruskal's Algorithm: {e}")
