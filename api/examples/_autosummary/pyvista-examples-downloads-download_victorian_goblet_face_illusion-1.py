from pyvista import examples
import pyvista as pv
mesh = examples.download_victorian_goblet_face_illusion()
plotter = pv.Plotter(lighting='none')
_ = plotter.add_mesh(
    mesh, edge_color='gray', color='white', show_edges=True
)
_ = plotter.add_floor('-x', color='black')
plotter.enable_parallel_projection()
plotter.show(cpos='yz')
#
# .. seealso::
#
#     :ref:`Victorian Goblet Face Illusion Dataset <victorian_goblet_face_illusion_dataset>`
