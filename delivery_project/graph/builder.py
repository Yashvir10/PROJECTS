import json
from src.graph.models import Node, Edge, Graph


def build_from_json(path: str) -> Graph:
    with open(path, "r") as f:
        data = json.load(f)

    graph = Graph()
    for n in data["nodes"]:
        graph.add_node(Node(**n))
    for e in data["edges"]:
        graph.add_edge(Edge(**e))
    return graph


def build_from_osm(place_name: str, network_type: str = "drive") -> Graph:
    import osmnx as ox

    osm_graph = ox.graph_from_place(place_name, network_type=network_type)
    graph = Graph()

    for node_id, data in osm_graph.nodes(data=True):
        graph.add_node(Node(id=str(node_id), lat=data["y"], lng=data["x"]))

    for u, v, data in osm_graph.edges(data=True):
        distance_km = data.get("length", 0) / 1000
        speed_kmh = 30  # assume avg city speed; refine later with data.get("maxspeed")
        time_min = (distance_km / speed_kmh) * 60
        graph.add_edge(Edge(str(u), str(v), distance_km, time_min), bidirectional=False)

    return graph