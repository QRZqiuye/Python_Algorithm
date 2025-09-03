import heapq
from typing import Dict, List, Tuple

Graph = Dict[str, List[Tuple[int, str]]]  # {정점: [(가중치, 인접정점), ...]}

def dijkstra(graph: Graph, start: str):
    """
    Dijkstra 최단 경로 알고리즘 (heapq 기반).
    - graph: {정점: [(가중치, 이웃정점), ...]}
    - start: 시작 정점
    반환: (거리 딕셔너리, 부모(경로 복원용) 딕셔너리)
    """
    # 초기화
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    parent = {start: None}

    pq = [(0, start)]  # (거리, 정점)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 이미 더 짧은 경로를 찾았다면 무시
        if current_dist > dist[u]:
            continue

        for weight, v in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, parent


def reconstruct_path(parent: Dict[str, str], target: str) -> List[str]:
    """parent 정보를 이용해 시작점 → target 최단 경로 복원"""
    path = []
    while target is not None:
        path.append(target)
        target = parent.get(target)
    return path[::-1]


# 사용 예시
if __name__ == "__main__":
    graph = {
        'A': [(7, 'B'), (9, 'C'), (14, 'F')],
        'B': [(7, 'A'), (10, 'C'), (15, 'D')],
        'C': [(9, 'A'), (10, 'B'), (11, 'D'), (2, 'F')],
        'D': [(15, 'B'), (11, 'C'), (6, 'E')],
        'E': [(6, 'D'), (9, 'F')],
        'F': [(14, 'A'), (2, 'C'), (9, 'E')],
    }

    dist, parent = dijkstra(graph, 'A')
    print("최단 거리:", dist)
    print("최단 경로 A→E:", reconstruct_path(parent, 'E'))
