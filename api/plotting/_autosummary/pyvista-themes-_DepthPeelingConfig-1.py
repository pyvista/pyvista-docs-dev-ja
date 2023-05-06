# Set global depth peeling parameters.
#
import pyvista as pv
pv.global_theme.depth_peeling.number_of_peels = 1
pv.global_theme.depth_peeling.occlusion_ratio = 0.0
pv.global_theme.depth_peeling.enabled = True
