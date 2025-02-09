# Create a bounding box for a dataset.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_oblique_cone()
box = mesh.bounding_box()
#
# Plot the mesh and its bounding box.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='red')
_ = pl.add_mesh(box, opacity=0.5)
pl.show()
#
# Create a frame instead.
#
frame = mesh.bounding_box('frame')
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='red')
_ = pl.add_mesh(frame, show_edges=True)
pl.show()
#
# Create an oriented bounding box (OBB) and compare it to the non-oriented one.
# Use the outline style for both.
#
box = mesh.bounding_box('outline')
obb = mesh.bounding_box('outline', oriented=True)
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(box, color='red', line_width=5)
_ = pl.add_mesh(obb, color='blue', line_width=5)
pl.show()
#
# Return the metadata for the box.
#
box, point, axes = mesh.bounding_box('outline', return_meta=True)
#
# Use the metadata to plot the box's axes using :class:`~pyvista.AxesAssembly`.
# Create the assembly and position it at the box's corner. Scale it to a fraction
# of the box's length.
#
scale = box.length / 4
axes_assembly = pv.AxesAssembly(position=point, scale=scale)
#
# Plot the box and the axes.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(box, color='black', line_width=5)
_ = pl.add_actor(axes_assembly)
_ = pl.view_yz()
pl.show()
