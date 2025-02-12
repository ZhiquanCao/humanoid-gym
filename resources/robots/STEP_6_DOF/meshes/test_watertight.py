import trimesh
import sys

# Check if a file path is provided
if len(sys.argv) < 2:
    print("Usage: python check_watertight.py <mesh_file>")
    sys.exit(1)

# Get the mesh file path from the first command-line argument
mesh_path = sys.argv[1]

# Load the mesh
mesh = trimesh.load(mesh_path)

# Check if the mesh is watertight
if mesh.is_watertight:
    print(f"✅ The mesh '{mesh_path}' is watertight (no holes).")
else:
    print(f"❌ The mesh '{mesh_path}' is NOT watertight (has holes).")

    # Find boundary edges (edges with missing faces)
    boundary_edges = mesh.edges[mesh.edges_unique[1] == 1]
    print(f"Mesh has {len(boundary_edges)} open edges (holes).")

