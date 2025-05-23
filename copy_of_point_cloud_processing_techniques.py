# -*- coding: utf-8 -*-
"""Copy of Point Cloud Processing Techniques.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bws3wxQhOQl0VTFhQddJRUd3l_dTiGI_
"""

!pip install pykdtree

!pip install open3d

from google.colab import drive
drive.mount('/content/drive')

"""# **Run**"""

import open3d as o3d
import numpy as np
Point_Cloud = o3d.io.read_point_cloud('/content/drive/MyDrive/Preprocesses_PC/point_cloud_00006.ply')
Point_Cloud_points = np.asarray(Point_Cloud.points)

Point_Cloud_points.shape

plane_model, inliers = Point_Cloud.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=2000)
# Extract the plane and outliers
plane = Point_Cloud.select_by_index(inliers)
outliers = Point_Cloud.select_by_index(inliers, invert=True)
plane_points = np.asarray(plane.points)
outliers_points = np.asarray(outliers.points)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(Point_Cloud_points[:, 0], Point_Cloud_points[:, 1], Point_Cloud_points[:, 2], s=1, c='green')
ax1.set_title('Generated (Fastener + Bridge) Point Cloud')
ax1.legend()

# Plot the segmented plane (inliers) in blue
ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(plane_points[:, 0], plane_points[:, 1], plane_points[:, 2], s=1, c='blue')
ax2.set_title('Outlier Bridge Region')
ax2.legend()

# Plot the outliers in red
ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(outliers_points[:, 0], outliers_points[:, 1], outliers_points[:, 2], s=1, c='red')
ax3.set_title('Extracted Fastener')
ax3.legend()

plt.show()

outliers_points.shape

point_cloud_segmented = o3d.geometry.PointCloud()
point_cloud_segmented.points = o3d.utility.Vector3dVector(outliers_points)

plane_model, inliers = point_cloud_segmented.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=2000)
# Extract the plane and outliers
plane = point_cloud_segmented.select_by_index(inliers)
outliers = point_cloud_segmented.select_by_index(inliers, invert=True)
plane_points = np.asarray(plane.points)
outliers_points_2 = np.asarray(outliers.points)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(outliers_points[:, 0], outliers_points[:, 1], outliers_points[:, 2], s=1, c='green')
ax1.set_title('Generated (Fastener + Bridge) Point Cloud')
ax1.legend()

# Plot the segmented plane (inliers) in blue
ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(plane_points[:, 0], plane_points[:, 1], plane_points[:, 2], s=1, c='blue')
ax2.set_title('Outlier Bridge Region')
ax2.legend()

# Plot the outliers in red
ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(outliers_points_2[:, 0], outliers_points_2[:, 1], outliers_points_2[:, 2], s=1, c='red')
ax3.set_title('Extracted Fastener')
ax3.legend()

plt.show()

outliers_points_2.shape

point_cloud_segmented = o3d.geometry.PointCloud()
point_cloud_segmented.points = o3d.utility.Vector3dVector(outliers_points_2)

plane_model, inliers = point_cloud_segmented.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=2000)
# Extract the plane and outliers
plane = point_cloud_segmented.select_by_index(inliers)
outliers = point_cloud_segmented.select_by_index(inliers, invert=True)
plane_points = np.asarray(plane.points)
outliers_points_3 = np.asarray(outliers.points)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(outliers_points_2[:, 0], outliers_points_2[:, 1], outliers_points_2[:, 2], s=1, c='green')
ax1.set_title('Generated (Fastener + Bridge) Point Cloud')
ax1.legend()

# Plot the segmented plane (inliers) in blue
ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(plane_points[:, 0], plane_points[:, 1], plane_points[:, 2], s=1, c='blue')
ax2.set_title('Outlier Bridge Region')
ax2.legend()

# Plot the outliers in red
ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(outliers_points_3[:, 0], outliers_points_3[:, 1], outliers_points_3[:, 2], s=1, c='red')
ax3.set_title('Extracted Fastener')
ax3.legend()

plt.show()

outliers_points_3.shape

point_cloud_segmented = o3d.geometry.PointCloud()
point_cloud_segmented.points = o3d.utility.Vector3dVector(outliers_points_3)

plane_model, inliers = point_cloud_segmented.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=2000)
# Extract the plane and outliers
plane = point_cloud_segmented.select_by_index(inliers)
outliers = point_cloud_segmented.select_by_index(inliers, invert=True)
plane_points = np.asarray(plane.points)
outliers_points_4 = np.asarray(outliers.points)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(outliers_points_3[:, 0], outliers_points_3[:, 1], outliers_points_3[:, 2], s=1, c='green')
ax1.set_title('Generated (Fastener + Bridge) Point Cloud')
ax1.legend()

# Plot the segmented plane (inliers) in blue
ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(plane_points[:, 0], plane_points[:, 1], plane_points[:, 2], s=1, c='blue')
ax2.set_title('Outlier Bridge Region')
ax2.legend()

# Plot the outliers in red
ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(outliers_points_4[:, 0], outliers_points_4[:, 1], outliers_points_4[:, 2], s=1, c='red')
ax3.set_title('Extracted Fastener')
ax3.legend()

plt.show()

outliers_points_4.shape

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(outliers_points)
# Save the point cloud to a PLY file
output_ply_filename = "/content/drive/MyDrive/Preprocesses_PC/point_cloud_00006.ply"
o3d.io.write_point_cloud(output_ply_filename, point_cloud)
print(f"Point cloud saved to {output_ply_filename}")

import os
# Define the directory where your point clouds are stored
directory = "/content/drive/MyDrive/Preprocesses_PC/"

# Get a list of all files in the directory
file_list = os.listdir(directory)

# Iterate through each file in the directory
for filename in file_list:
    # Check if the file is a PLY file
    if filename.endswith(".ply"):
        # Construct the full path to the file
        file_path = os.path.join(directory, filename)

        # Load the point cloud from the file
        point_cloud = o3d.io.read_point_cloud(file_path)

        # Calculate the number of points in the point cloud
        num_points = len(point_cloud.points)

        # Print the filename and the number of points
        print(f"File: {filename}, Number of Points: {num_points}")