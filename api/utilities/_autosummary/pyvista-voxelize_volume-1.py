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
