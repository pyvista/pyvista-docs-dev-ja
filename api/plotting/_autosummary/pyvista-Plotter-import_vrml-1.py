import pyvista
from pyvista import examples
sextant_file = (
    examples.vrml.download_sextant()
)  # doctest:+SKIP
pl = pyvista.Plotter()  # doctest:+SKIP
pl.import_vrml(sextant_file)  # doctest:+SKIP
pl.show()  # doctest:+SKIP
