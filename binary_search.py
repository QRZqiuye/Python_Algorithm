# 이진 탐색 알고리즘, 삽입 알고리즘, 삭제 알고리즘

# 1. 이진 탐색 알고리즘
def binary_search(arr, target):
    """
    이진 탐색: 정렬된 리스트 arr에서 target의 인덱스를 반환
    없으면 -1 반환
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


# 2. 삽입 알고리즘
def binary_insert(arr, value):
    """
    이진 탐색 기반 삽입:
    정렬 순서를 유지하면서 value 삽입
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    arr.insert(left, value)  # 올바른 위치에 삽입
    return arr


# 3. 삭제 알고리즘
def binary_delete(arr, value):
    """
    이진 탐색 기반 삭제:
    값이 존재하면 삭제, 없으면 그대로 반환
    """
    idx = binary_search(arr, value)
    if idx == -1:
        print("삭제할 원소가 존재하지 않습니다.")
        return arr
    arr.pop(idx)
    return arr


# 테스트 코드
data = [10, 20, 30, 40, 50]  # 정렬된 리스트

print("초기 데이터:", data)

# 탐색
idx = binary_search(data, 30)
print("30의 위치:", idx)

# 삽입
data = binary_insert(data, 35)  # 35 삽입
print("삽입 후:", data)

# 삭제
data = binary_delete(data, 20)  # 값 20 삭제
print("삭제 후:", data)
