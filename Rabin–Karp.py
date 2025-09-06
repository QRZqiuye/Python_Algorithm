def rabin_karp(T, P, d=256, q=101):
    """
    T: 텍스트 문자열
    P: 패턴 문자열
    d: 해시 계산을 위한 진법 (보통 256)
    q: 소수 (mod 연산용, 충돌 방지)
    """
    n, m = len(T), len(P)
    matches = []

    h = pow(d, m-1, q)  # 가장 높은 자리수의 값
    p_hash = 0  # 패턴 해시
    t_hash = 0  # 텍스트 윈도우 해시

    # 초기 해시값 계산
    for i in range(m):
        p_hash = (d * p_hash + ord(P[i])) % q
        t_hash = (d * t_hash + ord(T[i])) % q

    # 슬라이딩 윈도우
    for s in range(n - m + 1):
        # 해시값이 같으면 실제 문자열 비교
        if p_hash == t_hash:
            if T[s:s+m] == P:
                matches.append(s)

        # 다음 윈도우 해시 계산
        if s < n - m:
            t_hash = (d * (t_hash - ord(T[s]) * h) + ord(T[s+m])) % q
            if t_hash < 0:
                t_hash += q

    return matches


# 실행 예시
T = "ABC ABCDAB ABCDABCDABDE"
P = "ABCDABD"

result = rabin_karp(T, P)
print("패턴 발견 위치:", result)
