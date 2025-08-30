def insertion_sort_inplace(a: list) -> None:
    """
    리스트 a를 제자리(in-place)에서 삽입 정렬로 오름차순 정렬한다.

    반환값: None (원본 리스트 변경)
    시간복잡도: 평균/최악 O(n^2), 최선 O(n) (이미 정렬된 경우)
    공간복잡도: O(1)
    안정 정렬(stable)
    """
    for i in range(1, len(a)):
        key = a[i]  # 현재 삽입할 원소
        j = i - 1
        # key보다 큰 원소들은 한 칸씩 뒤로 이동
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        # key를 올바른 위치에 삽입
        a[j + 1] = key


def insertion_sort(a: list, *, key=None, reverse=False) -> list:
    """
    리스트 a의 복사본을 만들어 삽입 정렬한 결과를 반환한다.

    key: 비교를 위해 요소에서 값을 추출하는 함수 (예: lambda x: x[1])
    reverse: True이면 내림차순 정렬
    """
    if key is None:
        key = lambda x: x
    b = a[:]  # 원본 보존

    for i in range(1, len(b)):
        item = b[i]
        j = i - 1
        while j >= 0 and ((not reverse and key(b[j]) > key(item)) or
                          (reverse and key(b[j]) < key(item))):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = item
    return b

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("원본:", arr)

    insertion_sort_inplace(arr)
    print("삽입 정렬 (in-place):", arr)

    arr2 = [12, 11, 13, 5, 6]
    sorted_desc = insertion_sort(arr2, reverse=True)
    print("내림차순 정렬:", sorted_desc)

    people = [("Alice", 30), ("Bob", 22), ("Charlie", 25)]
    by_age = insertion_sort(people, key=lambda x: x[1])
    print("나이순 정렬:", by_age)
