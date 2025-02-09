import pyvista as pv
transform = pv.Transform().post_multiply()
transform.multiply_mode
# Expected:
## 'post'
