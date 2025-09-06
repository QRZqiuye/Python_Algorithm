def lz77_compress(text, window_size=20):
    """ LZ77 압축 알고리즘 """
    i = 0
    output = []

    while i < len(text):
        match = (-1, -1)  # (offset, length)
        # 윈도우 내에서 최장 매칭 찾기
        for j in range(max(0, i - window_size), i):
            length = 0
            while (i + length < len(text)) and text[j + length] == text[i + length]:
                length += 1
                if j + length >= i:
                    break
            if length > match[1]:
                match = (i - j, length)

        if match[1] > 0:
            next_char = text[i + match[1]] if i + match[1] < len(text) else ""
            output.append((match[0], match[1], next_char))
            i += match[1] + 1
        else:
            output.append((0, 0, text[i]))
            i += 1
    return output


def lz77_decompress(compressed):
    """ LZ77 해제 알고리즘 """
    output = []
    for offset, length, char in compressed:
        if offset == 0 and length == 0:
            output.append(char)
        else:
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
            if char:
                output.append(char)
    return "".join(output)


# 실행 예시
if __name__ == "__main__":
    text = "ABABCABABCD"
    print("원본 데이터:", text)

    compressed = lz77_compress(text)
    print("압축 결과:", compressed)

    decompressed = lz77_decompress(compressed)
    print("해제 결과:", decompressed)
