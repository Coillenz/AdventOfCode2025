from point import Point

import part_01.solve as part_01
import part_02.solve as part_02

def load_input(env: str) -> list[Point]:
    with open(f'day_09/{env}-input.txt') as input:
        points: list[Point] = []
        for line in input.read().splitlines():
            [x, y] = line.split(',')
            points.append(Point(int(x), int(y)))

        return points
    
points = load_input('test')
print('part_1 = ', part_01.find_largest_square_area(points))
print('part_2 = ', part_02.find_largest_connected_area(points))