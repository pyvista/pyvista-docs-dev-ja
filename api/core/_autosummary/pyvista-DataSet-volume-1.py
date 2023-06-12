# Get the volume of a cube of size 4x4x4.
# Note that there are 5 points in each direction.
#
import pyvista as pv
mesh = pv.ImageData(dimensions=(5, 5, 5))
mesh.volume
# Expected:
## 64.0
#
# A mesh with 2D cells has no volume.
#
mesh = pv.ImageData(dimensions=(5, 5, 1))
mesh.volume
# Expected:
## 0.0
#
# :class:`pyvista.PolyData` is special as a 2D surface can
# enclose a 3D volume.
#
mesh = pv.Sphere()
mesh.volume
# Expected:
## 0.51825
