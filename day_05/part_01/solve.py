def _exclude_unreachable_ranges(min_num: int, max_num: int, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    reachable_ranges: list[tuple[int, int]] = []
    for id_range in ranges:
        if max_num < id_range[0] or min_num > id_range[1]:
            continue

        reachable_ranges.append(id_range)
    
    return reachable_ranges


def find_fresh_ingredient_ids(ids: list[int], ranges: list[tuple[int, int]]) -> list[int]:
    possible_ranges = _exclude_unreachable_ranges(min(ids), max(ids), ranges)

    fresh_ids: list[int] = []
    for id_range in possible_ranges:
        for id in ids:
            if id in range(id_range[0], id_range[1] + 1) and id not in fresh_ids:
                fresh_ids.append(id)

    return fresh_ids