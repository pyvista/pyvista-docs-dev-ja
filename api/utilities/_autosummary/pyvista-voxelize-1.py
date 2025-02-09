# Create an equal density voxelized mesh.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_bunny_coarse().clean()
vox = pv.voxelize(mesh, density=0.01)
vox.plot(show_edges=True)
#
# Create a voxelized mesh using unequal density dimensions.
#
vox = pv.voxelize(mesh, density=[0.01, 0.005, 0.002])
vox.plot(show_edges=True)
#
# Create an equal density voxel volume without enclosing input mesh.
#
vox = pv.voxelize(mesh, density=0.01)
vox = vox.select_enclosed_points(mesh, tolerance=0.0)
vox.plot(scalars='SelectedPoints', show_edges=True)
#
# Create an equal density voxel volume enclosing input mesh.
#
vox = pv.voxelize(mesh, density=0.01, enclosed=True)
vox = vox.select_enclosed_points(mesh, tolerance=0.0)
vox.plot(scalars='SelectedPoints', show_edges=True)
#
# Create a voxelized mesh that does not fit the input mesh's bounds. Notice the
# cropped rectangular box.
#
mesh = pv.Cube(x_length=0.25)
vox = pv.voxelize(mesh=mesh, density=0.2)
pl = pv.Plotter()
_ = pl.add_mesh(mesh=vox, show_edges=True, color='yellow')
_ = pl.add_mesh(mesh=mesh, show_edges=True, line_width=5, opacity=0.4)
pl.show()
#
# Create a voxelized mesh that fits the input mesh's bounds. The rectangular mesh is
# now complete. Notice that the voxel size was updated to fit the bounds in the first
# direction.
#
vox = pv.voxelize(mesh=mesh, density=0.2, fit_bounds=True)
pl = pv.Plotter()
_ = pl.add_mesh(mesh=vox, show_edges=True, color='yellow')
_ = pl.add_mesh(mesh=mesh, show_edges=True, line_width=5, opacity=0.4)
pl.show()
