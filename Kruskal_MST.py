class UnionFind:
    """Disjoint Set Union (Union-Find) 자료구조"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def kruskal_mst(vertices, edges):
    """
    Kruskal 알고리즘으로 최소 신장 트리 구하기.
    - vertices: 정점 리스트 (ex: ['A','B','C'])
    - edges: (가중치, u, v) 튜플 리스트
    반환: (MST 가중치 합, MST 간선 리스트)
    """
    # 정점 → 인덱스 매핑
    idx = {v: i for i, v in enumerate(vertices)}
    uf = UnionFind(len(vertices))

    mst_weight = 0
    mst_edges = []

    # 간선 가중치 기준 정렬
    edges = sorted(edges, key=lambda x: x[0])

    for w, u, v in edges:
        if uf.union(idx[u], idx[v]):  # 사이클 없으면 MST에 포함
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges


# 사용 예시
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]

    weight, mst = kruskal_mst(vertices, edges)
    print("MST 가중치 합:", weight)
    print("MST 간선들:", mst)
