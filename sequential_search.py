# 순차 탐색 알고리즘, 삽입 알고리즘, 삭제 알고리즘

# 1. 순차 탐색 알고리즘
def sequential_search(arr, target):
    """
    순차 탐색: 리스트에서 target을 찾아 인덱스를 반환
    없으면 -1 반환
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. 삽입 알고리즘
def insert(arr, pos, value):
    """
    삽입 알고리즘: 리스트의 pos 위치에 value 삽입
    """
    if pos < 0 or pos > len(arr):
        print("삽입 위치가 올바르지 않습니다.")
        return arr
    arr.insert(pos, value)  # 내장함수 사용
    return arr


# 3. 삭제 알고리즘
def delete(arr, target):
    """
    삭제 알고리즘: 리스트에서 target을 찾아 삭제
    """
    pos = sequential_search(arr, target)
    if pos == -1:
        print("삭제할 원소가 존재하지 않습니다.")
        return arr
    arr.pop(pos)  # 해당 위치 원소 제거
    return arr


# 테스트 코드
data = [10, 20, 30, 40, 50]

print("초기 데이터:", data)

# 탐색
idx = sequential_search(data, 30)
print("30의 위치:", idx)

# 삽입
data = insert(data, 2, 25)  # 인덱스 2 위치에 25 삽입
print("삽입 후:", data)

# 삭제
data = delete(data, 40)  # 값 40 삭제
print("삭제 후:", data)
