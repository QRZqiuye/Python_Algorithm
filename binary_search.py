from typing import List, Any


def binary_search(arr: List[Any], target: Any) -> int:
    """
    이진 탐색 (Binary Search) - 반복문 버전
    arr: 오름차순 정렬된 리스트
    target: 찾을 값
    return: 찾으면 인덱스, 없으면 -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---- 사용 예시 ----
if __name__ == "__main__":
    data = [5, 7, 10, 23, 32, 62, 77, 88]
    print("데이터:", data)

    t1 = 23
    t2 = 99

    idx1 = binary_search(data, t1)
    print(f"{t1} 찾기 → 인덱스:", idx1)  # 3

    idx2 = binary_search(data, t2)
    print(f"{t2} 찾기 → 인덱스:", idx2)  # -1
