# Delivery Route Optimizer

An end-to-end route optimization system comparing **Dijkstra's algorithm** and **A\*** for delivery routing, optimized for either shortest distance or fastest time.

## Features
- Custom graph data structure (adjacency list) built from scratch
- Dijkstra and A* implementations with a shared interface for easy comparison
- Haversine-based heuristic for A* using real geographic coordinates
- FastAPI backend serving route computation over REST
- Streamlit + Folium frontend for interactive route visualization on a map
- Benchmark tooling comparing nodes expanded, runtime, and path cost between algorithms

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | FastAPI, Pydantic |
| Algorithms | Custom Dijkstra & A* (Python, heapq) |
| Graph data | Synthetic dataset / OpenStreetMap via osmnx |
| Frontend | Streamlit, Folium |
| Testing | Pytest |
| Analysis | Jupyter, Matplotlib, Pandas |

## Project Structure