from collections import deque
from typing import Dict, List, Hashable, Iterable, Tuple

Graph = Dict[Hashable, Iterable[Hashable]]

def bfs(graph: Graph, start) -> List:
    """
    큐를 사용한 BFS (연결된 한 구성요소만 탐색).
    - graph: {정점: [인접 정점, ...]}
    - start: 시작 정점
    반환: 방문 순서 리스트
    """
    visited = set([start])
    order = []
    queue = deque([start])  # 큐 초기화

    while queue:
        v = queue.popleft()
        order.append(v)

        neighbors = graph.get(v, [])
        neighbors = sorted(neighbors)  # 정렬 필요 없으면 제거하세요.
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                queue.append(n)

    return order


def bfs_full(graph: Graph) -> List:
    """
    그래프 전체(비연결 그래프 포함)를 BFS로 순회.
    각 구성요소의 시작점은 정점 키의 정렬 순서를 따름.
    """
    visited = set()
    order = []

    for start in sorted(graph.keys()):
        if start in visited:
            continue
        queue = deque([start])
        visited.add(start)

        while queue:
            v = queue.popleft()
            order.append(v)

            neighbors = graph.get(v, [])
            neighbors = sorted(neighbors)
            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

    return order


def bfs_with_parent(graph: Graph, start) -> Tuple[List, Dict]:
    """
    BFS 트리(부모 정보)까지 함께 반환.
    반환: (방문 순서, parent 딕셔너리)
    parent[start] = None
    """
    visited = set([start])
    order = []
    parent = {start: None}
    queue = deque([start])

    while queue:
        v = queue.popleft()
        order.append(v)

        neighbors = graph.get(v, [])
        neighbors = sorted(neighbors)
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                parent[n] = v
                queue.append(n)

    return order, parent


# 사용 예시
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': ['H'],   # 분리된 구성요소
        'H': ['G']
    }

    print("단일 시작점 BFS(A):", bfs(graph, 'A'))
    print("전체 BFS(비연결 포함):", bfs_full(graph))
    order, parent = bfs_with_parent(graph, 'A')
    print("방문 순서:", order)
    print("부모(BFS 트리):", parent)
