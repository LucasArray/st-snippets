def find_duplicates(items):
    freq_map = {}
    for item in items:
        freq_map[item] = freq_map.get(item, 0) + 1
    return {
        item: count for item, count in freq_map.items()
        if count > 1
    }