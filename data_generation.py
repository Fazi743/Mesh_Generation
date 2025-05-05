
from google.colab import drive
drive.mount('/content/drive')

!pip install open3d

import open3d as o3d
import numpy as np
point_cloud1 = o3d.io.read_point_cloud("/content/drive/MyDrive/+---¦·¦+-º+¦-¦8¦++¦+¦¦++»-²+¦.2023.6 (1).13/point cloud/point_cloud_00021 (1).ply")

import open3d as o3d
import numpy as np

# Generate a sample point cloud (replace this with your actual point cloud)
np.random.seed(42)

# Create an Open3D point cloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.asarray(point_cloud1.points))

# Estimate normals for the point cloud
pcd.estimate_normals()

# Create a mesh from the point cloud
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

"""# preprocessng"""

mesh.remove_duplicated_vertices()
mesh.remove_degenerate_triangles()
# Normalize the mesh
mesh.translate(-mesh.get_center())
# Smooth the mesh
mesh = mesh.filter_smooth_taubin(number_of_iterations=10)
mesh2 = mesh.simplify_quadric_decimation(50000)

"""# **Segmentation**"""

import open3d as o3d
import numpy as np
import pandas as pd
# Load the mesh

# Generate random cluster labels (replace this with your actual cluster labels)
num_clusters = len(list(pd.Series( mesh2.cluster_connected_triangles()[0]).unique()))
cluster_labels = np.array(list(mesh2.cluster_connected_triangles()[0]))
# num_clusters = 3
# cluster_labels = np.array([0, 1, 7])


# Create a list to store the meshes for each cluster
cluster_meshes = []

# Iterate over each cluster
for cluster_id in range(num_clusters):
    # Extract the indices of triangles belonging to the current cluster
    cluster_indices = np.where(cluster_labels == cluster_id)[0]

    # Create a new mesh for the current cluster
    cluster_mesh = o3d.geometry.TriangleMesh()
    cluster_mesh.vertices = mesh2.vertices
    triangle_list = [list(np.array(mesh2.triangles)[i]) for i in cluster_indices]
    triangles_ = o3d.utility.Vector3iVector(triangle_list)
    cluster_mesh.triangles = triangles_

    # Colorize the cluster
    color = np.random.rand(3)
    cluster_mesh.paint_uniform_color(color)

    # Append the cluster mesh to the list
    #cluster_meshes.append(cluster_mesh)
    o3d.io.write_triangle_mesh(f'CLUSTER_{cluster_id}_mesh.ply', cluster_mesh)

!mv "/content/CLUSTER_1_mesh.ply" "/content/drive/MyDrive/Mesh Generated Data/Meshs 3D"

!cp "/content/drive/MyDrive/+---¦·¦+-º+¦-¦8¦++¦+¦¦++»-²+¦.2023.6 (1).13/image/rgb_image_00030.jpg" "/content/drive/MyDrive/Mesh Generated Data/Fastener Images"

!cp "/content/drive/MyDrive/+---¦·¦+-º+¦-¦8¦++¦+¦¦++»-²+¦.2023.6 (1).13/depth/depth_image_00030.tiff" "/content/drive/MyDrive/Mesh Generated Data/Fastener Depth"

!cp "/content/drive/MyDrive/+---¦·¦+-º+¦-¦8¦++¦+¦¦++»-²+¦.2023.6 (1).13/point cloud/point_cloud_00030 (1).ply" "/content/drive/MyDrive/Mesh Generated Data/Point Clouds"

"""# **Normal**"""





