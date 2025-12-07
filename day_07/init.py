import threading

import part_01.solve as part_01
import part_02.solve as part_02

def visualize(grid: list[list[str]], hits: list[tuple[int, int]]):
  for hit in hits:
    grid[hit[1]][hit[0]] = 'X'

  for line in grid:
    print(''.join(line))

def load_input(env: str) -> tuple[list[list[str]], int]:
  with open(f'day_07/{env}-input.txt') as input:
    start_pos = 0
    grid: list[list[str]] = []

    for line in input.readlines():
      grid.append(list(line.strip()))

    for idx, char in enumerate(grid[0]):
      if char == 'S':
        start_pos = idx
        break

    return (grid, start_pos)

[grid, start_pos] = load_input('real')
result_1 = part_01.calculate_tachyon_hits(grid, start_pos)
visualize(grid, result_1)
print("part_01: ", len(result_1))

result_2 = part_02.calculate_tachyon_timelines(result_1)
print('part_02: ', result_2)