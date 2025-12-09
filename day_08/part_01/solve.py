from edge import Edge

def calculate_closest_edges(edges: list[Edge]) -> list[tuple[float, Edge, Edge]]:
    edge_distances: list[tuple[float, Edge, Edge]] = []
    for curr_edge_idx, edge in enumerate(edges):
        for idx in range(len(edges)):
            if idx == curr_edge_idx:
                continue

            distance = edge.distance_to_edge(edges[idx])
            if ((distance, edge, edges[idx]) in edge_distances or (distance, edges[idx], edge)) in edge_distances:
                continue

            edge_distances.append((distance, edge, edges[idx]))
    
    return sorted(edge_distances, key=lambda distance: distance[0])

def find_longest_circuits(edges: list[Edge]) -> dict[int, list[Edge]]:
    # Get the edge distances sorted by shortest
    edge_distances = calculate_closest_edges(edges)

    print(edge_distances)
    return {}