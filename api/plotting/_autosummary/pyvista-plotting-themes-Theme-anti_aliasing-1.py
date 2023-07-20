# Use super-sampling anti-aliasing in the global theme.
#
import pyvista as pv
pv.global_theme.anti_aliasing = 'ssaa'
pv.global_theme.anti_aliasing
# Expected:
## 'ssaa'
#
# Disable anti-aliasing in the global theme.
#
import pyvista as pv
pv.global_theme.anti_aliasing = None
#
# See :ref:`anti_aliasing_example` for more information regarding
