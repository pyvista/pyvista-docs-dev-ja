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
