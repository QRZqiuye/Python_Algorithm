from typing import List, Any

def sequential_search(arr: List[Any], target: Any) -> int:
    """
    순차 탐색 (Linear Search)
    arr: 탐색할 리스트
    target: 찾을 값
    return: 찾으면 해당 인덱스, 없으면 -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---- 사용 예시 ----
if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]
    print("데이터:", data)

    t1 = 23
    t2 = 100

    idx1 = sequential_search(data, t1)
    print(f"{t1} 찾기 → 인덱스:", idx1)  # 2

    idx2 = sequential_search(data, t2)
    print(f"{t2} 찾기 → 인덱스:", idx2)  # -1
