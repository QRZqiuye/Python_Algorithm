def lcs(X, Y):
    m, n = len(X), len(Y)
    # DP 테이블 초기화
    dp = [[0] * (n+1) for _ in range(m+1)]

    # DP 채우기
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # LCS 문자열 추적
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()  # 역순이므로 뒤집기
    return dp[m][n], "".join(lcs_str)


# 실행 예시
X = "ABCBDAB"
Y = "BDCAB"

length, sequence = lcs(X, Y)
print("LCS 길이:", length)
print("LCS:", sequence)
