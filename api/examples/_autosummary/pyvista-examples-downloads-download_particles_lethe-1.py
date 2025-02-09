# Download the particles dataset and plot it after generating glyphs.
#
from pyvista import examples
particles = examples.download_particles_lethe()
particles.plot(
    render_points_as_spheres=True,
    style='points',
    scalars='Velocity',
    background='w',
    scalar_bar_args={'color': 'k'},
    cmap='bwr',
)
#
# .. seealso::
#
#     :ref:`Particles Lethe Dataset <particles_lethe_dataset>`
