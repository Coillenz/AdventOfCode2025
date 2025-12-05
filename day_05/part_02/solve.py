def find_possible_fresh_ingredient_ids(ranges: list[tuple[int, int]]) -> list[int]:
    found_ids: list[int] = []
    
    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            if id not in found_ids:
                found_ids.append(id)

    return found_ids