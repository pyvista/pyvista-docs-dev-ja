# Save a pyvista sphere to a Abaqus data file.
#
import pyvista as pv
sphere = pv.Sphere()
pv.save_meshio('mymesh.inp', sphere)  # doctest:+SKIP
