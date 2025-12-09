from edge import Edge

import part_01.solve as part_01

def load_input(env: str):
    with open(f'day_08/{env}-input.txt') as input:
        edges: list[Edge] = []
        for line in input.read().splitlines():
            dimensions = line.split(',')
            edges.append(Edge(int(dimensions[0]), int(dimensions[1]), int(dimensions[2])))

        return edges
    
graph = load_input('test')
print(part_01.find_longest_circuits(graph))