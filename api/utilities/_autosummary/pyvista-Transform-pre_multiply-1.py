import pyvista as pv
transform = pv.Transform().pre_multiply()
transform.multiply_mode
# Expected:
## 'pre'
