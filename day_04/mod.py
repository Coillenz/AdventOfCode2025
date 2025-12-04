import math
import part_01.solve as part_01
import part_02.solve as part_02

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

        for line in [line.replace('\n', '') for line in input.readlines()]:
            if line_width == 0:
                line_width = len(line)

            line_result: list[int] = []
            for char in line:
                line_result.append(ord(char))
        
            result.extend(line_result)

        return (result, line_width)

[input, line_width] = prepare_input('real')
print('Part 1 result', len(part_01.count_accessible_rolls(input, line_width)))
print('Part 2 result', len(part_02.count_all_accessible_rolls(input, line_width)))