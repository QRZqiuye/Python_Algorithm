def shell_sort(a: list) -> None:
    """
    리스트 a를 제자리(in-place)에서 셸 정렬로 오름차순 정렬한다.

    반환값: None (원본 리스트 변경)
    시간복잡도: 최악 O(n^2), 평균 O(n log^2 n) 정도 (gap 선택에 따라 달라짐)
    공간복잡도: O(1)
    안정 정렬 아님 (stable X)
    """
    n = len(a)
    gap = n // 2  # 초기 간격은 배열 길이의 절반

    # gap을 줄여가며 삽입 정렬 수행
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            # gap 간격으로 삽입 정렬 수행
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2  # 간격 줄임


if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    print("원본:", arr)

    shell_sort(arr)
    print("셸 정렬 결과:", arr)

    arr2 = [64, 34, 25, 12, 22, 11, 90]
    shell_sort(arr2)
    print("정렬 결과:", arr2)
