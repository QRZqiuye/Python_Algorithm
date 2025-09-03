from typing import Dict, List, Tuple

Edge = Tuple[str, str, int]   # (출발, 도착, 가중치)
Graph = List[Edge]

def bellman_ford(vertices: List[str], edges: Graph, start: str):
    """
    벨만-포드 알고리즘
    - vertices: 정점 리스트
    - edges: (u, v, w) 형태의 간선 리스트
    - start: 시작 정점
    반환: (거리 딕셔너리, 부모 딕셔너리)
    음수 사이클이 있으면 ValueError 발생
    """
    # 거리 초기화
    dist = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    dist[start] = 0

    # (V-1)번 반복
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break  # 더 이상 갱신이 없으면 종료

    # 음수 사이클 탐지
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("음수 사이클이 존재하여 최단 경로가 정의되지 않음")

    return dist, parent


def reconstruct_path(parent: Dict[str, str], target: str) -> List[str]:
    """parent 정보를 이용해 start → target 최단 경로 복원"""
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]


# 사용 예시
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', -1),
        ('B', 'D', 2),
        ('C', 'D', 3),
        ('C', 'E', 2),
        ('D', 'E', -5)
    ]

    try:
        dist, parent = bellman_ford(vertices, edges, 'A')
        print("최단 거리:", dist)
        print("A→E 최단 경로:", reconstruct_path(parent, 'E'))
    except ValueError as e:
        print(e)
