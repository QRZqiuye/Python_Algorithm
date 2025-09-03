import heapq
from typing import Dict, List, Tuple

Graph = Dict[str, List[Tuple[int, str]]]  # {정점: [(가중치, 이웃정점), ...]}

def prim_mst(graph: Graph, start: str):
    """
    Prim 알고리즘으로 MST 구하기.
    - graph: {정점: [(가중치, 이웃정점), ...]}
    - start: 시작 정점
    반환: (MST 가중치 합, MST 간선 리스트)
    """
    visited = set()
    mst_edges = []
    mst_weight = 0

    # (가중치, 시작정점, 끝정점) 형태의 우선순위 큐
    edges = [(w, start, v) for w, v in graph[start]]
    heapq.heapify(edges)

    visited.add(start)

    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        # 간선 선택
        visited.add(v)
        mst_weight += w
        mst_edges.append((u, v, w))

        # 새로운 정점 v에서 나가는 간선 추가
        for w2, nxt in graph[v]:
            if nxt not in visited:
                heapq.heappush(edges, (w2, v, nxt))

    return mst_weight, mst_edges


# 사용 예시
if __name__ == "__main__":
    graph = {
        'A': [(7, 'B'), (5, 'D')],
        'B': [(7, 'A'), (8, 'C'), (9, 'D'), (7, 'E')],
        'C': [(8, 'B'), (5, 'E')],
        'D': [(5, 'A'), (9, 'B'), (7, 'E'), (6, 'F')],
        'E': [(7, 'B'), (5, 'C'), (7, 'D'), (8, 'F'), (9, 'G')],
        'F': [(6, 'D'), (8, 'E'), (11, 'G')],
        'G': [(9, 'E'), (11, 'F')]
    }

    weight, mst = prim_mst(graph, 'A')
    print("MST 가중치 합:", weight)
    print("MST 간선들:", mst)
