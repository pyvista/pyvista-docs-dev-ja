# Create a bounding box for a dataset.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_oblique_cone()
box = mesh.oriented_bounding_box()
#
# Plot the mesh and its bounding box.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='red')
_ = pl.add_mesh(box, opacity=0.5)
pl.show()
#
# Return the metadata for the box.
#
box, point, axes = mesh.oriented_bounding_box('outline', return_meta=True)
#
# Use the metadata to plot the box's axes using :class:`~pyvista.AxesAssembly`.
# The assembly is aligned with the x-y-z axes and positioned at the origin by
# default. Create a transformation to scale, then rotate, then translate the
# assembly to the corner point of the box. The transpose of the axes is used
# as an inverted rotation matrix.
#
scale = box.length / 4
transform = pv.Transform().scale(scale).rotate(axes.T).translate(point)
axes_assembly = pv.AxesAssembly(user_matrix=transform.matrix)
#
# Plot the box and the axes.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(box, color='black', line_width=5)
_ = pl.add_actor(axes_assembly)
pl.show()
#
# Note how the box's z-axis is pointing from the cone's tip to its base. If we
# want to flip this axis, we can "seed" its direction as the ``'-z'`` direction.
#
box, _, axes = mesh.oriented_bounding_box(
    'outline', axis_2_direction='-z', return_meta=True
)
#
# Plot the box and axes again. This time, use :class:`~pyvista.AxesAssemblySymmetric`
# and position the axes in the center of the box.
#
center = pv.merge(box).points.mean(axis=0)
scale = box.length / 2
transform = pv.Transform().scale(scale).rotate(axes.T).translate(center)
axes_assembly = pv.AxesAssemblySymmetric(user_matrix=transform.matrix)
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(box, color='black', line_width=5)
_ = pl.add_actor(axes_assembly)
pl.show()
