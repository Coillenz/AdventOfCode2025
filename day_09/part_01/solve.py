from point import Point

def find_largest_square_area(points: list[Point]) -> int:
    areas: list[tuple[int, Point, Point]] = []
    for curr_point_index, curr_point in enumerate(points):
        for point_idx, point in enumerate(points):
            if point_idx == curr_point_index or point_idx - 1 == curr_point_index:
                continue

            areas.append((curr_point.get_area(point), curr_point, point))

    print(max(areas, key=lambda area: area[0]))

    largest_square = max(areas, key=lambda area: area[0])
    return largest_square[0]