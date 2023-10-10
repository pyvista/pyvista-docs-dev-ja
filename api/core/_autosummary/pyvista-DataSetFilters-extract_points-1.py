# Extract all the points of a sphere with a Z coordinate greater than 0
#
import pyvista as pv
sphere = pv.Sphere()
extracted = sphere.extract_points(
    sphere.points[:, 2] > 0, include_cells=False
)
extracted.clear_data()  # clear for plotting
extracted.plot()
