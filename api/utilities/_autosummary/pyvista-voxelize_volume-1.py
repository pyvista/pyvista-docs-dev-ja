# Create an equal density voxel volume from input mesh.
#
import pyvista as pv
import numpy as np
#
# Load file from PyVista examples.
#
from pyvista import examples
mesh = examples.download_cow()
#
# Create an equal density voxel volume and plot the result.
#
vox = pv.voxelize_volume(mesh, density=0.15)
cpos = [(15, 3, 15), (0, 0, 0), (0, 0, 0)]
vox.plot(scalars='InsideMesh', show_edges=True, cpos=cpos)
#
# Slice the voxel volume to view ``InsideMesh``.
#
slices = vox.slice_orthogonal()
slices.plot(scalars='InsideMesh', show_edges=True)
#
# Create a voxel volume from unequal density dimensions and plot result.
#
vox = pv.voxelize_volume(mesh, density=[0.15, 0.15, 0.5])
vox.plot(scalars='InsideMesh', show_edges=True, cpos=cpos)
#
# Slice the unequal density voxel volume to view ``InsideMesh``.
#
slices = vox.slice_orthogonal()
slices.plot(scalars='InsideMesh', show_edges=True, cpos=cpos)
#
# Create an equal density voxel volume without enclosing input mesh.
#
vox = pv.voxelize_volume(mesh, density=0.15)
vox = vox.select_enclosed_points(mesh, tolerance=0.0)
vox.plot(scalars='SelectedPoints', show_edges=True, cpos=cpos)
#
# Create an equal density voxel volume enclosing input mesh.
#
vox = pv.voxelize_volume(mesh, density=0.15, enclosed=True)
vox = vox.select_enclosed_points(mesh, tolerance=0.0)
vox.plot(scalars='SelectedPoints', show_edges=True, cpos=cpos)
#
# Create an equal density voxel volume that does not fit the input mesh's bounds.
#
mesh = pv.examples.load_nut()
vox = pv.voxelize_volume(mesh=mesh, density=2.5)
pl = pv.Plotter()
_ = pl.add_mesh(mesh=vox, show_edges=True)
_ = pl.add_mesh(mesh=mesh, show_edges=True, opacity=1)
pl.show()
#
# Create an equal density voxel volume that fits the input mesh's bounds.
#
vox = pv.voxelize_volume(mesh=mesh, density=2.5, fit_bounds=True)
pl = pv.Plotter()
_ = pl.add_mesh(mesh=vox, show_edges=True)
_ = pl.add_mesh(mesh=mesh, show_edges=True, opacity=1)
pl.show()
