# Generate a :class:`pyvista.UnstructuredGrid` with many tetrahedrons
# nearby each other and plot it without SSAO.
#
import pyvista as pv
ugrid = pv.UniformGrid(dimensions=(3, 2, 2)).to_tetrahedra(12)
exploded = ugrid.explode()
exploded.plot()
#
# Enable SSAO with the default parameters.
#
pl = pv.Plotter()
_ = pl.add_mesh(exploded)
pl.enable_ssao()
pl.show()
