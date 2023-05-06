# Set roughness to 0.1
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'
prop.metallic = 0.5  # helps to visualize metallic
prop.roughness = 0.1
prop.roughness
# Expected:
## 0.1
#
# Visualize default roughness with metallic of ``0.5``.
#
prop.roughness = 0.5
prop.plot()
#
# Visualize roughness at ``0.0`` with metallic of ``0.5``.
#
prop.roughness = 0.0
prop.plot()
#
# Visualize roughness at ``1.0`` with metallic of ``0.5``.
#
prop.roughness = 1.0
prop.plot()
