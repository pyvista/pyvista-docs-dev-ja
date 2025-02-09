# Create a dataset and align it to the x-y-z axes.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_oblique_cone()
aligned = mesh.align_xyz()
#
# Plot the aligned mesh along with the original. Show axes at the origin for
# context.
#
axes = pv.AxesAssembly(scale=aligned.length)
pl = pv.Plotter()
_ = pl.add_mesh(aligned)
_ = pl.add_mesh(mesh, style='wireframe', color='black', line_width=3)
_ = pl.add_actor(axes)
pl.show()
#
# Align the mesh but don't center it.
#
aligned = mesh.align_xyz(centered=False)
#
# Plot the result again. The aligned mesh has the same position as the input.
#
axes = pv.AxesAssembly(position=mesh.center, scale=aligned.length)
pl = pv.Plotter()
_ = pl.add_mesh(aligned)
_ = pl.add_mesh(mesh, style='wireframe', color='black', line_width=3)
_ = pl.add_actor(axes)
pl.show()
#
# Note how the tip of the cone is pointing along the z-axis. This indicates that
# the cone's axis is the third principal axis. It is also pointing in the negative
# z-direction. To control the alignment so that the cone points upward, we can
# seed an approximate direction specifying what "up" means for the original mesh
# in world coordinates prior to the alignment.
#
# We can see that the cone is originally pointing downward, somewhat in the
# negative z-direction. Therefore, we can specify the ``'-z'`` vector
# as the "up" direction of the mesh's third axis prior to alignment.
#
aligned = mesh.align_xyz(axis_2_direction='-z')
#
# Plot the mesh. The cone is now pointing upward in the desired direction.
#
axes = pv.AxesAssembly(scale=aligned.length)
pl = pv.Plotter()
_ = pl.add_mesh(aligned)
_ = pl.add_actor(axes)
pl.show()
#
# The specified direction only needs to be approximate. For example, we get the
# same result by specifying the ``'y'`` direction as the mesh's original "up"
# direction.
#
aligned, matrix = mesh.align_xyz(axis_2_direction='y', return_matrix=True)
axes = pv.AxesAssembly(scale=aligned.length)
pl = pv.Plotter()
_ = pl.add_mesh(aligned)
_ = pl.add_actor(axes)
pl.show()
#
# We can optionally return the transformation matrix.
#
aligned, matrix = mesh.align_xyz(axis_2_direction='y', return_matrix=True)
#
# The matrix can be inverted, for example, to transform objects from the world
# axes back to the original mesh's local coordinate system.
#
inverse = pv.Transform(matrix).inverse_matrix
#
# Use the inverse to label the object's axes prior to alignment. For actors,
# we set the :attr:`~pyvista.Prop3D.user_matrix` as the inverse.
#
axes_local = pv.AxesAssembly(
    scale=aligned.length,
    user_matrix=inverse,
    labels=["X'", "Y'", "Z'"],
)
#
# Plot the original mesh with its local axes, along with the algned mesh and its
# axes.
#
axes_aligned = pv.AxesAssembly(scale=aligned.length)
pl = pv.Plotter()
_ = pl.add_mesh(aligned)
_ = pl.add_actor(axes_aligned)
_ = pl.add_mesh(mesh, style='wireframe', color='black', line_width=3)
_ = pl.add_actor(axes_local)
pl.show()
