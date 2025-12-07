def calculate_tachyon_timelines(hits: list[tuple[int, int]]) -> int:
  hit_grid: list[list[int]] = []

  last_line = 0
  for hit in sorted(hits, key=lambda hit: hit[1]):
    if hit[1] > last_line:
      hit_grid.append([])
      last_line = hit[1]

    hit_grid[-1].append(hit[0])
  
  for line in hit_grid:
    line.sort()

  return calculate_tachyon_timelines_recursive(hit_grid, 0, hit_grid[0][0])

def calculate_tachyon_timelines_recursive(hit_grid: list[list[int]], curr_line: int, curr_pos: int) -> int:
  if curr_line == len(hit_grid):
    return 1
  
  if curr_pos in hit_grid[curr_line]:
    timelines = calculate_tachyon_timelines_recursive(hit_grid, curr_line + 1, curr_pos - 1)
    timelines += calculate_tachyon_timelines_recursive(hit_grid, curr_line + 1, curr_pos + 1)
    return timelines
  
  return calculate_tachyon_timelines_recursive(hit_grid, curr_line + 1, curr_pos)
