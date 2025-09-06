import sys

def matrix_chain_order(p):
    """
    p: 행렬 차원 리스트 (길이가 n+1)
       예: 행렬 A1: 10x30, A2: 30x5, A3: 5x60
           p = [10, 30, 5, 60]
    """
    n = len(p) - 1  # 행렬 개수
    # 최소 곱셈 횟수를 저장할 테이블
    m = [[0] * n for _ in range(n)]
    # 최적의 분할 위치를 저장할 테이블
    s = [[0] * n for _ in range(n)]

    # l은 체인 길이 (2개 행렬부터 n개 행렬까지)
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    """ 최적 괄호 구조 출력 """
    if i == j:
        return f"A{i+1}"
    else:
        return "(" + print_optimal_parens(s, i, s[i][j]) + " x " + print_optimal_parens(s, s[i][j]+1, j) + ")"

# 실행 예시
p = [10, 30, 5, 60]  # A1: 10x30, A2: 30x5, A3: 5x60
m, s = matrix_chain_order(p)

print("최소 곱셈 횟수:", m[0][len(p)-2])
print("최적 괄호 구조:", print_optimal_parens(s, 0, len(p)-2))
