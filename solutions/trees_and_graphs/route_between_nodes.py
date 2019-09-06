"""
Problem

    Given a directed graph, design an algorithm to find out whether there is a
    route between nodes.
"""
from typing import Dict

Node = int


def is_route_exists(
    graph: Dict, source: Node, destination: Node, visited=None
) -> bool:
    """Find route between two nodes

    This method implements Depth First Search (DFS) algorithm. It keeps track
    of visited nodes to avoid cycles.

    If given source node or destination node is not present in a graph then
    this method instantly terminates by assuming that there are no route
    between given source and destination node in given graph.
    """
    if visited is None:
        visited = set()
    if source == destination:
        return True
    elif len(visited) == len(graph):
        return False
    visited.add(source)
    try:
        for next_source in graph[source]:
            if next_source not in visited:
                if is_route_exists(
                    graph, next_source, destination, visited
                ):
                    return True
    except KeyError:
        return False
    return False
