# Get the area of a square of size 2x2.
# Note 5 points in each direction.
#
import pyvista as pv
mesh = pv.ImageData(dimensions=(5, 5, 1))
mesh.area
# Expected:
## 16.0
#
# A mesh with 3D cells does not have an area.  To get
# the outer surface area, first extract the surface using
# :func:`pyvista.DataSetFilters.extract_surface`.
#
mesh = pv.ImageData(dimensions=(5, 5, 5))
mesh.area
# Expected:
## 0.0
#
# Get the area of a sphere.
#
mesh = pv.Sphere()
mesh.volume
# Expected:
## 0.51825
