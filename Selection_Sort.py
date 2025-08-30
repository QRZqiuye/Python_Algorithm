# 선택 정렬(제자리, 기본 오름차순)
def selection_sort_inplace(a: list) -> None:
    """
    리스트 a를 제자리(in-place)에서 오름차순으로 정렬한다.
    반환값: None (원본 리스트가 변경됨)
    시간복잡도: O(n^2), 공간복잡도: O(1)
    주의: 안정 정렬(stable)이 아니다.
    """
    n = len(a)
    for i in range(n - 1):
        # i 위치에 올 최소값의 인덱스를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 최소값을 i 위치로 교환
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]


# 범용 선택 정렬: key, reverse 옵션 지원, 새 리스트 반환
def selection_sort(a: list, *, key=None, reverse=False) -> list:
    """
    리스트 a의 복사본을 만들어 선택 정렬로 정렬한 새로운 리스트를 반환한다.
    key: 비교를 위해 요소에서 값을 추출하는 함수 (예: lambda x: x[1])
    reverse: True이면 내림차순으로 정렬
    시간복잡도: O(n^2)
    """
    if key is None:
        key = lambda x: x
    b = a[:]  # 원본 보존
    n = len(b)
    for i in range(n - 1):
        sel_idx = i
        for j in range(i + 1, n):
            # 비교 기준값
            if reverse:
                # 내림차순: 현재가 선택된 값보다 더 크면 교체
                if key(b[j]) > key(b[sel_idx]):
                    sel_idx = j
            else:
                # 오름차순: 현재가 선택된 값보다 더 작으면 교체
                if key(b[j]) < key(b[sel_idx]):
                    sel_idx = j
        if sel_idx != i:
            b[i], b[sel_idx] = b[sel_idx], b[i]
    return b


# ---------------------------
# 예시 사용법
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("원본:", arr)

    # 제자리 정렬
    selection_sort_inplace(arr)
    print("in-place 정렬 후:", arr)

    # 원본 보존하고 새 리스트 반환 (내림차순 예시)
    arr2 = [64, 25, 12, 22, 11]
    sorted_desc = selection_sort(arr2, reverse=True)
    print("원본 보존:", arr2)
    print("내림차순 정렬 (새 리스트):", sorted_desc)

    # key 사용 예시 (튜플 리스트를 두번째 항목 기준으로 오름차순)
    people = [("A", 30), ("B", 22), ("C", 25)]
    by_age = selection_sort(people, key=lambda x: x[1])
    print("나이순 정렬:", by_age)
