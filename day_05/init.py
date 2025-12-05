from typing import cast

import part_01.solve as part_01
import part_02.solve as part_02

def load_input(env: str) -> tuple[list[int], list[tuple[int, int]]]:
    with open(f'day_05/{env}-input.txt') as input:
        lines = input.readlines()
        split_idx = lines.index('\n')

        ids =  [int(line.strip()) for line in lines[split_idx + 1:]]
        ranges =  cast(list[tuple[int, int]] , [list(map(int, line.strip().split('-'))) for line in lines[:split_idx]])
        return (ids, ranges)
    
[ids, ranges] = load_input('real')
print(len(part_01.find_fresh_ingredient_ids(ids, ranges)))
print(part_02.count_possible_fresh_ingredient_ids(ranges))