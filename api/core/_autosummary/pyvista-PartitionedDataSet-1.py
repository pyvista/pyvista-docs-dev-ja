import pyvista as pv
data = [
    pv.Sphere(center=(2, 0, 0)),
    pv.Cube(center=(0, 2, 0)),
    pv.Cone(),
]
partitions = pv.PartitionedDataSet(data)
len(partitions)
# Expected:
## 3
