# Join two meshes together, extract the largest, and plot it.
#
import pyvista as pv
mesh = pv.Sphere() + pv.Cube()
largest = mesh.extract_largest()
largest.plot()
#
# See :ref:`connectivity_example` and :ref:`volumetric_example` for
# more examples using this filter.
#
# .. seealso::
