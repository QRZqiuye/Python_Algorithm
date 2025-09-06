def compute_lps(pattern):
    """ 패턴에 대한 LPS(Longest Prefix Suffix) 배열 계산 """
    lps = [0] * len(pattern)
    length = 0  # 이전 접두사-접미사 일치 길이
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """ KMP 문자열 검색 """
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches = []

    i = j = 0  # i = 텍스트 인덱스, j = 패턴 인덱스
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:  # 패턴 발견
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


# 실행 예시
T = "ABC ABCDAB ABCDABCDABDE"
P = "ABCDABD"

result = kmp_search(T, P)
print("패턴 발견 위치:", result)
