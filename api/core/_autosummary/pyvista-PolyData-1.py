import vtk
import numpy as np
from pyvista import examples
import pyvista as pv
#
# Seed random number generator for reproducible plots
#
rng = np.random.default_rng(seed=0)
#
# Create an empty mesh.
#
mesh = pv.PolyData()
#
# Initialize from a ``vtk.vtkPolyData`` object.
#
vtkobj = vtk.vtkPolyData()
mesh = pv.PolyData(vtkobj)
#
# Initialize from just points, creating vertices
#
points = np.array([[0, 0, 0], [1, 0, 0], [1, 0.5, 0], [0, 0.5, 0]])
mesh = pv.PolyData(points)
#
# Initialize from points and faces, creating polygonal faces.
#
faces = np.hstack([[3, 0, 1, 2], [3, 0, 3, 2]])
mesh = pv.PolyData(points, faces)
#
# Initialize from points and lines.
#
lines = np.hstack([[2, 0, 1], [2, 1, 2]])
mesh = pv.PolyData(points, lines=lines)
#
# Initialize from points and triangle strips.
#
strips = np.hstack([[4, 0, 1, 3, 2]])
mesh = pv.PolyData(points, strips=strips)
#
# It is also possible to create with multiple cell types.
#
verts = [1, 0]
lines = [2, 1, 2]
mesh = pv.PolyData(points, verts=verts, lines=lines)
#
# Initialize from a filename.
#
mesh = pv.PolyData(examples.antfile)
#
# Construct a set of random line segments using a ``pv.CellArray`.
# Because every line in this example has the same size, in this case
# two points, we can use ``pv.CellArray.from_regular_cells`` to
# construct the ``lines`` cell array. This is the most efficient
# method to construct a cell array.
#
n_points = 20
n_lines = n_points // 2
points = rng.random((n_points, 3))
lines = rng.integers(low=0, high=n_points, size=(n_lines, 2))
mesh = pv.PolyData(points, lines=pv.CellArray.from_regular_cells(lines))
mesh.cell_data['line_idx'] = np.arange(n_lines)
mesh.plot(scalars='line_idx')
#
# Construct a set of random triangle strips using a ``pv.CellArray``.
# Because each strip in this example can have a different number
# of points, we use ``pv.CellArray.from_irregular_cells`` to construct
# the ``strips`` cell array.
#
n_strips = 4
n_verts_per_strip = rng.integers(low=3, high=7, size=n_strips)
n_points = 10 * sum(n_verts_per_strip)
points = rng.random((n_points, 3))
strips = [
    rng.integers(low=0, high=n_points, size=nv) for nv in n_verts_per_strip
]
mesh = pv.PolyData(
    points, strips=pv.CellArray.from_irregular_cells(strips)
)
mesh.cell_data['strip_idx'] = np.arange(n_strips)
mesh.plot(show_edges=True, scalars='strip_idx')
#
# Construct a mesh reusing the ``faces`` ``pv.CellArray`` from another
# mesh. The VTK methods ``GetPolys``, ``GetLines``, ``GetStrips``, and
# ``GetVerts`` return the underlying ``CellArray``s for the ``faces``,
# ``lines``, ``strips``, and ``verts`` properties respectively.
# Reusing cell arrays like this can be a performance optimization for
# large meshes because it avoids allocating new arrays.
#
small_sphere = pv.Sphere().compute_normals()
inflated_points = (
    small_sphere.points + 0.1 * small_sphere.point_data['Normals']
)
larger_sphere = pv.PolyData(inflated_points, faces=small_sphere.GetPolys())
plotter = pv.Plotter()
_ = plotter.add_mesh(small_sphere, color='red', show_edges=True)
_ = plotter.add_mesh(
    larger_sphere, color='blue', opacity=0.3, show_edges=True
)
plotter.show()
