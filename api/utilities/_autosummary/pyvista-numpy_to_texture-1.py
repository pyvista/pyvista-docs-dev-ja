# Create an all white texture.
#
import pyvista as pv
import numpy as np
tex_arr = np.ones((1024, 1024, 3), dtype=np.uint8) * 255
tex = pv.numpy_to_texture(tex_arr)
