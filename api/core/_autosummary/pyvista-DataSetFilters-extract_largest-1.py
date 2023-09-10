# Join two meshes together, extract the largest, and plot it.
#
import pyvista
mesh = pyvista.Sphere() + pyvista.Cube()
largest = mesh.extract_largest()
largest.plot()
#
# See :ref:`connectivity_example` and :ref:`volumetric_example` for
# more examples using this filter.
#
# .. seealso::
