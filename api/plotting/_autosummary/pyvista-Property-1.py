# Create a :class:`pyvista.Actor` and assign properties to it.
#
import pyvista as pv
actor = pv.Actor()
actor.prop = pv.Property(
    color='r',
    show_edges=True,
    interpolation='Physically based rendering',
    metallic=0.5,
    roughness=0.1,
)
#
# Visualize how the property would look when applied to a mesh.
#
actor.prop.plot()
#
# Set custom properties not directly available in
# :func:`pyvista.Plotter.add_mesh`. Here, we set diffuse, ambient, and
# specular power and colors.
#
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
prop = actor.prop
prop.diffuse = 0.6
prop.diffuse_color = 'w'
prop.ambient = 0.3
prop.ambient_color = 'r'
prop.specular = 0.5
prop.specular_color = 'b'
pl.show()
