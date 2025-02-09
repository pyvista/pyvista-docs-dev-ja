# Get the default roughness value.
#
import pyvista as pv
prop = pv.Property()
prop.roughness
# Expected:
## 0.5
#
# Visualize default roughness with metallic of ``0.5`` and physically-based
# rendering.
#
prop.interpolation = 'pbr'
prop.metallic = 0.5
prop.plot()
#
# Visualize roughness at ``0.1``.
#
prop.roughness = 0.0
prop.plot()
#
# Visualize roughness at ``1.0``.
#
prop.roughness = 1.0
prop.plot()
