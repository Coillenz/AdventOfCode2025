def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = sorted(ranges, key=lambda id_range: id_range[0])
    merged_ranges: list[tuple[int, int]] = []
    
    current_merged_range = sorted_ranges[0]
    for curr_range in sorted_ranges:
        if current_merged_range[1] >= curr_range[0]:
            current_merged_range[1] = max(current_merged_range[1], curr_range[1])
            continue

        merged_ranges.append(current_merged_range)
        current_merged_range = curr_range

    merged_ranges.append(current_merged_range)
    return merged_ranges

def count_possible_fresh_ingredient_ids(ranges: list[tuple[int, int]]) -> int:
    found_id_count = 0
    
    merged_ranges = merge_ranges(ranges)
    for id_range in merged_ranges:
        found_id_count += len(range(id_range[0], id_range[1] + 1))

    return found_id_count