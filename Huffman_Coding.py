import heapq
from collections import Counter, namedtuple

# 허프만 트리 노드 정의
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq  # 우선순위 큐에서 빈도 기준 비교


def build_huffman_tree(data: str):
    """ 허프만 트리 생성 """
    freq = Counter(data)
    heap = [Node(ch, fr, None, None) for ch, fr in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]  # 루트 노드 반환


def build_codes(node, prefix="", code_map=None):
    """ 허프만 코드 생성 (재귀 탐색) """
    if code_map is None:
        code_map = {}

    if node.char is not None:  # 리프 노드
        code_map[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)

    return code_map


def huffman_encode(data: str, code_map):
    """ 허프만 인코딩 """
    return "".join(code_map[ch] for ch in data)


def huffman_decode(encoded: str, root):
    """ 허프만 디코딩 """
    decoded = []
    node = root
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char is not None:  # 리프 노드 도달
            decoded.append(node.char)
            node = root
    return "".join(decoded)


# 실행 예시
if __name__ == "__main__":
    text = "aaabccdeeeeeffg"
    print("원본 데이터:", text)

    # 허프만 트리 생성
    root = build_huffman_tree(text)
    codes = build_codes(root)
    print("허프만 코드:", codes)

    # 인코딩
    encoded = huffman_encode(text, codes)
    print("압축 결과 (비트열):", encoded)

    # 디코딩
    decoded = huffman_decode(encoded, root)
    print("해제 결과:", decoded)
