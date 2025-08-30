def advanced_bubble_sort(a: list) -> None:
    """
    리스트 a를 제자리(in-place)에서 개선된 버블 정렬로 오름차순 정렬한다.
    반환값: None (원본 리스트 변경)
    시간복잡도: 최악 O(n^2), 최선 O(n), 보통 경우 일반 버블 정렬보다 빠름
    공간복잡도: O(1)
    안정 정렬(stable)
    """
    n = len(a)
    while n > 1:
        new_n = 0  # 마지막 교환이 발생한 위치
        for i in range(1, n):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                new_n = i  # 마지막 교환 위치 갱신
        n = new_n  # 다음 패스에서는 new_n까지만 비교

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("원본:", arr)

    advanced_bubble_sort(arr)
    print("개선된 버블 정렬:", arr)

    arr2 = [1, 2, 3, 4, 5]
    print("이미 정렬된 배열:", arr2)
    advanced_bubble_sort(arr2)
    print("정렬 후:", arr2)
