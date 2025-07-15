def count_occurrences(items):
    freq_map = {}
    for item in items:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map