from collections import Counter
from math import log2


def calculate_entropy(data):
    total_count = len(data)
    counts = Counter(data)
    entropy = 0.0

    for count in counts.values():
        probability = count / total_count
        entropy -= probability * log2(probability)

    return entropy
