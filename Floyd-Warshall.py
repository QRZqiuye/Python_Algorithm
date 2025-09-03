from typing import List, Dict, Any

def floyd_warshall(vertices: List[str], graph: Dict[str, Dict[str, int]]):
    """
    Floyd-Warshall 알고리즘 (모든 정점 쌍 최단 경로)
    - vertices: 정점 리스트
    - graph: {u: {v: w}} 형태 (없는 경로는 INF로 취급)
    반환: dist, next_node
        dist[u][v] = 최단 거리
        next_node[u][v] = 최단 경로에서 u 다음에 오는 정점
    """
    INF = float('inf')
    n = len(vertices)
    dist = {u: {v: INF for v in vertices} for u in vertices}
    next_node = {u: {v: None for v in vertices} for u in vertices}

    # 초기화
    for u in vertices:
        dist[u][u] = 0
        if u in graph:
            for v, w in graph[u].items():
                dist[u][v] = w
                next_node[u][v] = v

    # 점화식
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # 음수 사이클 탐지
    for v in vertices:
        if dist[v][v] < 0:
            raise ValueError("음수 사이클 존재")

    return dist, next_node


def reconstruct_path(next_node, u: str, v: str) -> List[str]:
    """Floyd-Warshall 결과로 u→v 최단 경로 복원"""
    if next_node[u][v] is None:
        return []  # 경로 없음
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path


# 사용 예시
if __name__ == "__main__":
    vertices = ["A", "B", "C", "D"]
    graph = {
        "A": {"B": 3, "C": 7},
        "B": {"C": -2},
        "C": {"D": 2},
        "D": {"A": 6}
    }

    try:
        dist, next_node = floyd_warshall(vertices, graph)
        print("최단 거리 행렬:")
        for u in vertices:
            print(u, dist[u])
        print("A→D 최단 경로:", reconstruct_path(next_node, "A", "D"))
    except ValueError as e:
        print(e)
