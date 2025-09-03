from collections import defaultdict
from typing import Dict, List, Hashable, Iterable, Tuple

Graph = Dict[Hashable, Iterable[Hashable]]

def dfs_stack(graph: Graph, start) -> List:
    """
    스택을 사용한 DFS (연결 구성요소 하나를 탐색).
    - graph: {정점: [인접정점, ...]}
    - start: 시작 정점
    반환: 방문 순서 리스트
    """
    visited = set()
    order = []
    stack = [start]  # 스택 최상단이 리스트 끝

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        order.append(v)

        # 재귀 DFS와 동일한 방문 순서를 원하면, 인접 정점을 '역순'으로 push
        # (스택은 후입선출이므로 역순으로 넣어야 작은 것부터 먼저 pop됨)
        neighbors = graph.get(v, [])
        # 정렬이 필요 없으면 아래 줄을 제거하세요.
        neighbors = sorted(neighbors, reverse=True)
        for n in neighbors:
            if n not in visited:
                stack.append(n)

    return order

def dfs_stack_full(graph: Graph) -> List:
    """
    그래프 전체(비연결 그래프 포함)를 DFS로 순회하여 방문 순서를 반환.
    정점 키의 정렬된 순서대로 각 구성요소의 시작점을 선택(일관된 결과 위해).
    """
    visited = set()
    order = []

    for start in sorted(graph.keys()):
        if start in visited:
            continue
        # 구성요소별 스택 DFS
        stack = [start]
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            order.append(v)

            neighbors = graph.get(v, [])
            neighbors = sorted(neighbors, reverse=True)
            for n in neighbors:
                if n not in visited:
                    stack.append(n)

    return order

def dfs_with_parent(graph: Graph, start) -> Tuple[List, Dict]:
    """
    부모(DFS 트리) 정보까지 함께 반환하는 스택 DFS.
    반환: (방문순서, parent 딕셔너리)  parent[root]는 None
    """
    visited = set()
    order = []
    parent = {start: None}
    stack = [start]

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        order.append(v)

        neighbors = graph.get(v, [])
        neighbors = sorted(neighbors, reverse=True)
        for n in neighbors:
            if n not in visited:
                if n not in parent:
                    parent[n] = v
                stack.append(n)

    return order, parent


# 사용 예시
if __name__ == "__main__":
    # 무향 그래프 예시
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

    print("단일 시작점 DFS(A):", dfs_stack(graph, 'A'))
    print("전체 DFS(비연결 포함):", dfs_stack_full(graph))
    order, parent = dfs_with_parent(graph, 'A')
    print("방문 순서:", order)
    print("부모(DFS 트리):", parent)
