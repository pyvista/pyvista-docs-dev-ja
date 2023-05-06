# Show the number of components in the example masonry texture.
#
from pyvista import examples
texture = examples.download_masonry_texture()
texture.n_components
# Expected:
## 3
