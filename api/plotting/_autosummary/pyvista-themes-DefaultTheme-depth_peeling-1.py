# Set the global depth_peeling parameter default to be enabled
# with 8 peels.
#
import pyvista as pv
pv.global_theme.depth_peeling.number_of_peels = 8
pv.global_theme.depth_peeling.occlusion_ratio = 0.0
pv.global_theme.depth_peeling.enabled = True
