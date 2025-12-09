from point import Point

def point_is_invalid(point1: Point, point2: Point, current_point: Point):
    return ((point2.x - point1.x) * (current_point.x - point1.x)) <= ((point2.x - point1.x) * current_point.x - point1.x)

def get_convex_hull(points: list[Point]) -> list[Point]:
    """
    Convex hull algorithm for calculating the outer border for the polygon
    
    :param points: The points to get the outer hull for
    :type points: list[Point]
    :return: The outer hull points
    :rtype: list[Point]
    """
    hull = [points[0]]
    for point in points:
        while len(hull) > 1 and point_is_invalid(hull[-2], hull[-1], point):
            hull.pop()

        hull.append(point)
    return hull

def find_largest_square_area(points: list[Point]) -> int:
    areas: list[tuple[int, Point, Point]] = []
    for curr_point_index, curr_point in enumerate(points):
        for point_idx, point in enumerate(points):
            if point_idx == curr_point_index or point_idx - 1 == curr_point_index:
                continue

            areas.append((curr_point.get_area(point), curr_point, point))

    largest_square = max(areas, key=lambda area: area[0])

    print(largest_square)
    return largest_square[0]

def find_largest_connected_area(points: list[Point]) -> int:
    sorted_points = sorted(points, key=lambda point: point.x)
    vertices = get_convex_hull(sorted_points) + get_convex_hull(sorted_points[::-1])[1:]

    print(len(points))
    print(len(vertices))
    return find_largest_square_area(vertices)