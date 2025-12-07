def calculate_tachyon_timelines(hits: list[tuple[int, int]]) -> int:
  hit_grid: list[list[int]] = []

  last_line = 0
  for hit_pos in sorted(hits, key=lambda hit: hit[1]):
    if hit_pos[1] > last_line:
      hit_grid.append([])
      last_line = hit_pos[1]

    hit_grid[-1].append(hit_pos[0])

  highest_idx = max(map(lambda line: max(line), [*hit_grid]))

  timeline_map: list[int] = list()
  for _ in range(highest_idx + 2):
    timeline_map.append(0)

  timeline_map[hit_grid[0][0]] = 1

  for line in hit_grid:
    for hit_pos in line:
      timeline_map[hit_pos - 1] += timeline_map[hit_pos]
      timeline_map[hit_pos + 1] += timeline_map[hit_pos]
      timeline_map[hit_pos] = 0

  print(sum(timeline_map))