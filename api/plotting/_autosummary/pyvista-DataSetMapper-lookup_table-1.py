# Return the lookup table of a dataset mapper.
#
import pyvista as pv
mesh = pv.Sphere()
pl = pv.Plotter()
actor = pl.add_mesh(mesh, scalars=mesh.points[:, 2], cmap='bwr')
actor.mapper.lookup_table
# Expected:
## LookupTable (...)
##   Table Range:                (-0.5, 0.5)
##   N Values:                   256
##   Above Range Color:          None
##   Below Range Color:          None
##   NAN Color:                  Color(name='darkgray', hex='#a9a9a9ff', opacity=255)
##   Log Scale:                  False
##   Color Map:                  "bwr"
#
# Return the lookup table of a composite dataset mapper.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.lookup_table  # doctest:+SKIP
# Expected:
## <vtkmodules.vtkCommonCore.vtkLookupTable(...) at ...>
