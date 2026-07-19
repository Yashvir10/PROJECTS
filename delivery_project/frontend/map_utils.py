import folium
from src.graph.models import Graph


def render_graph_map(graph: Graph, path: list[str] = None, center: tuple = None):
    if center is None:
        first_node = next(iter(graph.nodes.values()))
        center = (first_node.lat, first_node.lng)

    m = folium.Map(location=center, zoom_start=13)

    # Draw all nodes
    for node in graph.nodes.values():
        is_on_path = path and node.id in path
        folium.CircleMarker(
            location=(node.lat, node.lng),
            radius=6 if is_on_path else 4,
            color="red" if is_on_path else "gray",
            fill=True,
            fill_color="red" if is_on_path else "gray",
            popup=f"{node.name or node.id}",
        ).add_to(m)

    # Draw all edges (light gray, background)
    seen = set()
    for node_id, edges in graph.adjacency.items():
        for edge in edges:
            key = tuple(sorted([edge.from_node, edge.to_node]))
            if key in seen:
                continue
            seen.add(key)
            n1 = graph.get_node(edge.from_node)
            n2 = graph.get_node(edge.to_node)
            folium.PolyLine(
                locations=[(n1.lat, n1.lng), (n2.lat, n2.lng)],
                color="lightgray",
                weight=2,
            ).add_to(m)

    # Draw the computed path (highlighted)
    if path and len(path) > 1:
        coords = [(graph.get_node(nid).lat, graph.get_node(nid).lng) for nid in path]
        folium.PolyLine(locations=coords, color="blue", weight=5, opacity=0.8).add_to(m)

    return m