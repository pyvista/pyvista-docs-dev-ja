from pyvista import examples
dataset = examples.download_tri_quadratic_hexahedron()
dataset.plot()
#
# Show non-linear subdivision.
#
surf = dataset.extract_surface(nonlinear_subdivision=5)
surf.plot(smooth_shading=True)
