import pyvista as pv
from pyvista import examples
#
mesh = examples.download_tri_quadratic_hexahedron()
surface_sep = mesh.separate_cells().extract_surface(
    nonlinear_subdivision=4
)
edges = surface_sep.extract_feature_edges()
surface = mesh.extract_surface(nonlinear_subdivision=4)
#
plotter = pv.Plotter()
_ = plotter.add_mesh(surface, smooth_shading=True, split_sharp_edges=True)
actor = plotter.add_mesh(edges, color='k', line_width=3)
actor.mapper.resolve = 'polygon_offset'
plotter.show()
