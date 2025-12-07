def calculate_tachyon_hits(grid: list[list[str]], current_pos: int) -> set[tuple[int, int]]:
  return calculate_tachyon_hits_recursive(grid, 0, current_pos, set())

def calculate_tachyon_hits_recursive(grid: list[list[str]], current_line: int, current_pos: int, hits: set[tuple[int, int]]):
  if current_pos < 0 or current_pos >= len(grid[current_line]):
    return set()

  if current_line == len(grid) - 1:
    return set()
  
  if grid[current_line][current_pos] == '^':
    if (current_pos, current_line) in hits:
      return hits
    
    hits.add((current_pos, current_line))
    hits.update(calculate_tachyon_hits_recursive(grid, current_line, current_pos - 1, hits))
    hits.update(calculate_tachyon_hits_recursive(grid, current_line, current_pos + 1, hits))
    return hits
  
  return calculate_tachyon_hits_recursive(grid, current_line + 1, current_pos, hits)