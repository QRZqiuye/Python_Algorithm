def bubble_sort_inplace(a: list) -> None:
    """
    리스트 a를 제자리(in-place)에서 오름차순으로 정렬한다.
    반환값: None (원본 리스트 변경)
    시간복잡도: O(n^2) (최악/평균), 최선은 O(n) (이미 정렬된 경우)
    공간복잡도: O(1)
    안정 정렬(stable)
    """
    n = len(a)
    for i in range(n - 1):
        swapped = False  # 이번 패스에서 교환 여부
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:  # 교환이 없으면 이미 정렬 완료
            break

def bubble_sort(a: list, *, key=None, reverse=False) -> list:
    """
    리스트 a의 복사본을 만들어 버블 정렬 후 반환한다.
    key: 비교를 위해 요소에서 값을 추출하는 함수 (예: lambda x: x[1])
    reverse: True이면 내림차순으로 정렬
    """
    if key is None:
        key = lambda x: x

    b = a[:]  # 원본 보존
    n = len(b)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if (not reverse and key(b[j]) > key(b[j + 1])) or \
               (reverse and key(b[j]) < key(b[j + 1])):
                b[j], b[j + 1] = b[j + 1], b[j]
                swapped = True
        if not swapped:
            break
    return b


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("원본:", arr)

    # 제자리 정렬
    bubble_sort_inplace(arr)
    print("in-place 정렬:", arr)

    # 원본 보존, 내림차순 정렬
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    sorted_desc = bubble_sort(arr2, reverse=True)
    print("원본 보존:", arr2)
    print("내림차순 정렬:", sorted_desc)

    # key 사용 (튜플 리스트를 나이 기준으로 오름차순)
    people = [("Alice", 30), ("Bob", 22), ("Charlie", 25)]
    by_age = bubble_sort(people, key=lambda x: x[1])
    print("나이순 정렬:", by_age)
