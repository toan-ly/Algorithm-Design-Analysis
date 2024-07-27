import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Count frequency of each character
    frequency = Counter(text)
    
    # Create a priority queue of HuffmanNodes
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root of the Huffman tree

def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = current_code
        return
    
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)
    
    return codes

# Create the text based on the given frequencies
text = "a" * 80 + "b" * 65 + "c" * 55 + "d" * 60 + "e" * 105 + "f" * 35 + "g" * 5 + " " * 30

# Build the Huffman tree and generate codes
root = build_huffman_tree(text)
huffman_codes = generate_huffman_codes(root)

# Print the Huffman codes
for char, code in sorted(huffman_codes.items()):
    print(f"'{char}': {code}")

# Calculate the average code length
total_bits = sum(len(code) * text.count(char) for char, code in huffman_codes.items())
average_length = total_bits / len(text)
print(f"\nAverage code length: {average_length:.2f} bits")