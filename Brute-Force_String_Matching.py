def brute_force_string_match(T, P):
    n, m = len(T), len(P)
    matches = []

    for i in range(n - m + 1):  # 가능한 시작 위치
        j = 0
        while j < m and T[i + j] == P[j]:
            j += 1
        if j == m:  # 패턴 전체가 매칭됨
            matches.append(i)
    return matches


# 실행 예시
T = "ABC ABCDAB ABCDABCDABDE"
P = "ABCDABD"

result = brute_force_string_match(T, P)
print("패턴 발견 위치:", result)
