# Combine blocks within a multiblock without merging points.
#
import pyvista as pv
block = pv.MultiBlock(
    [
        pv.Cube(clean=False),
        pv.Cube(center=(1, 0, 0), clean=False),
    ]
)
merged = block.combine()
merged.n_points
# Expected:
## 48
#
# Combine blocks and merge points
#
merged = block.combine(merge_points=True)
merged.n_points
# Expected:
## 12
