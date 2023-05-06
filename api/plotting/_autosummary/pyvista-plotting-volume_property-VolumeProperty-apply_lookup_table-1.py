# Plot perlin noise volumetrically using a custom lookup table.
#
import pyvista as pv
noise = pv.perlin_noise(1, (1, 3, 5), (0, 0, 0))
grid = pv.sample_function(
    noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(40, 40, 40)
)
grid['scalars'] -= grid['scalars'].min()
grid['scalars'] *= 255 / grid['scalars'].max()
pl = pv.Plotter()
actor = pl.add_volume(grid, show_scalar_bar=False)
lut = pv.LookupTable(cmap='bwr')
lut.apply_opacity([1.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.3])
actor.prop.apply_lookup_table(lut)
pl.show()
