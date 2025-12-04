import math

paper_char = ord('@')
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

def visualize_result(result: list[int], input: list[int], line_width: int):
    result_buffer: list[str] = [''] * len(input)
    for idx in range(len(input)):
        result_buffer[idx] = chr(input[idx])

    for found_idx in result:
        result_buffer[found_idx] = 'X'
    
    result_matrix: list[list[str]] = []
    for line_idx in range(math.floor(len(result_buffer) / line_width)):
        current_buffer_idx = line_idx * line_width
        result_matrix.append(result_buffer[current_buffer_idx:current_buffer_idx + line_width])

    result_str_buffer: list[str] = []
    for line in result_matrix:
        result_str_buffer.append(''.join(line))
        
    print('\n'.join(result_str_buffer))
    print('\nResult: ', len(result))
        
    
def prepare_input(environment: str) -> tuple[list[int], int]:
    with open(f'day_04/{environment}-input.txt') as input:
        result: list[int] = []
        line_width: int = 0

        for line in map(lambda line: line.replace('\n', ''), input.readlines()):
            if line_width == 0:
                line_width = len(line)

            line_result: list[int] = []
            for char in line:
                line_result.append(ord(char))
        
            result.extend(line_result)

        return (result, line_width)

[input, line_width] = prepare_input('real')
result = count_accessible_rolls(input, line_width)
visualize_result(result, input, line_width)