def rle_encode(data: str) -> str:
    """ RLE 압축 """
    if not data:
        return ""

    encoded = []
    count = 1
    prev = data[0]

    for ch in data[1:]:
        if ch == prev:
            count += 1
        else:
            encoded.append(prev + str(count))
            prev = ch
            count = 1
    encoded.append(prev + str(count))  # 마지막 문자 처리
    return "".join(encoded)


def rle_decode(data: str) -> str:
    """ RLE 해제 """
    decoded = []
    char = ""
    count = ""

    for ch in data:
        if ch.isalpha():  # 문자
            if char and count:  # 이전 문자 처리
                decoded.append(char * int(count))
                count = ""
            char = ch
        else:  # 숫자
            count += ch

    if char and count:
        decoded.append(char * int(count))

    return "".join(decoded)


# 실행 예시
text = "aaabbbccccdaa"
encoded = rle_encode(text)
decoded = rle_decode(encoded)

print("원본:", text)
print("압축:", encoded)
print("해제:", decoded)
