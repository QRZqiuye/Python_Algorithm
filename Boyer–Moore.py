def bad_char_table(pattern):
    """ 패턴의 각 문자에 대해 마지막 등장 위치를 기록 """
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def boyer_moore_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    bad_char = bad_char_table(pattern)
    matches = []

    s = 0  # 패턴의 시작 위치
    while s <= n - m:
        j = m - 1

        # 패턴과 텍스트를 오른쪽에서 왼쪽으로 비교
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:  # 패턴 매칭 성공
            matches.append(s)
            # 다음 위치로 이동 (패턴이 겹치지 않게)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            # 불일치 발생 → 점프
            s += max(1, j - bad_char.get(text[s + j], -1))

    return matches


# 실행 예시
T = "ABC ABCDAB ABCDABCDABDE"
P = "ABCDABD"

result = boyer_moore_search(T, P)
print("패턴 발견 위치:", result)
