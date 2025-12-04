import math

paper_char = ord('@')
found_char = ord('X')
diameter = 3

def is_surrounded_by_4_rolls(idx: int, input: list[int], line_width: int):
    paper_count = 0
    radius = math.floor(diameter / 2)

    for y in range(-radius, diameter - radius):
        current_line = int(idx / line_width) + y
        if current_line < 0 or current_line > (len(input) / line_width) - 1:
            continue
        
        for x in range(-radius, diameter - radius):
            if y == 0 and x == 0:
                continue

            current_line_pos = (idx % line_width) + x
            if current_line_pos < 0 or current_line_pos > line_width - 1:
                continue

            current_search_pos = idx + (line_width * y) + x
            if input[current_search_pos] == paper_char:
                paper_count += 1

                if paper_count == 4:
                    return True

    return False

def count_accessible_rolls(input: list[int], line_width: int) -> list[int]:
    found_rolls_positions: list[int] = []

    for idx, item in enumerate(input):
        if item != paper_char:
            continue

        if not is_surrounded_by_4_rolls(idx, input, line_width):
            found_rolls_positions.append(idx)
    
    return found_rolls_positions

def count_all_accessible_rolls(input: list[int], line_width: int) -> list[int]:
    current_input = input.copy()
    found_rolls_positions: list[int] = []

    while True:
        found_rolls_positions_temp = count_accessible_rolls(current_input, line_width)
        if len(found_rolls_positions_temp) == 0:
            break

        found_rolls_positions.extend(found_rolls_positions_temp)
        for idx in found_rolls_positions_temp:
            current_input[idx] = found_char
    
    return found_rolls_positions