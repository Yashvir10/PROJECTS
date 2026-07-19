import streamlit as st
import requests
from streamlit_folium import st_folium
from src.graph.builder import build_from_json
from frontend.map_utils import render_graph_map

st.set_page_config(page_title="Delivery Route Optimizer", layout="wide")
st.title("🚚 Delivery Route Optimizer")

API_URL = "http://127.0.0.1:8000/route"

# Load graph once (cached across reruns)
@st.cache_resource
def load_graph():
    return build_from_json("data/sample_graph.json")

graph = load_graph()
node_ids = list(graph.nodes.keys())
node_labels = {nid: f"{nid} - {graph.nodes[nid].name}" for nid in node_ids}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Route Settings")

    start = st.selectbox("Start location", node_ids, format_func=lambda x: node_labels[x])
    end = st.selectbox("End location", node_ids, index=len(node_ids) - 1, format_func=lambda x: node_labels[x])
    algorithm = st.radio("Algorithm", ["dijkstra", "astar"])
    mode = st.radio("Optimize for", ["time", "distance"])

    if st.button("Find Route", type="primary"):
        if start == end:
            st.warning("Start and end must be different.")
        else:
            try:
                response = requests.post(
                    API_URL,
                    json={"start": start, "end": end, "algorithm": algorithm, "mode": mode},
                    timeout=5,
                )
                if response.status_code == 200:
                    st.session_state["result"] = response.json()
                else:
                    st.error(f"Error: {response.json().get('detail')}")
            except requests.exceptions.ConnectionError:
                st.error("Could not reach API. Make sure it's running: `uvicorn src.api.main:app --reload`")

    if "result" in st.session_state:
        result = st.session_state["result"]
        st.divider()
        st.metric("Total Cost", f"{result['cost']:.2f} {'min' if mode == 'time' else 'km'}")
        st.metric("Nodes Expanded", result["nodes_expanded"])
        st.write("**Path:**", " → ".join(result["path"]))

with col2:
    st.subheader("Map")
    path = st.session_state.get("result", {}).get("path")
    fmap = render_graph_map(graph, path=path)
    st_folium(fmap, width=700, height=500)