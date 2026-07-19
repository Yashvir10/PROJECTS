from dataclasses import dataclass, field


@dataclass
class Node:
    id: str
    lat: float
    lng: float
    name: str = ""


@dataclass
class Edge:
    from_node: str
    to_node: str
    distance: float  # km
    time: float       # minutes

    def weight(self, mode: str = "time") -> float:
        return self.time if mode == "time" else self.distance


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.adjacency: dict[str, list[Edge]] = {}

    def add_node(self, node: Node):
        self.nodes[node.id] = node
        self.adjacency.setdefault(node.id, [])

    def add_edge(self, edge: Edge, bidirectional: bool = True):
        self.adjacency.setdefault(edge.from_node, []).append(edge)
        if bidirectional:
            reverse = Edge(edge.to_node, edge.from_node, edge.distance, edge.time)
            self.adjacency.setdefault(edge.to_node, []).append(reverse)

    def neighbors(self, node_id: str) -> list[Edge]:
        return self.adjacency.get(node_id, [])

    def get_node(self, node_id: str) -> Node:
        return self.nodes[node_id]