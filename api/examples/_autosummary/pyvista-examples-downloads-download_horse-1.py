from pyvista import examples
dataset = examples.download_horse()
dataset.plot(smooth_shading=True)
#
# See :ref:`disabling_mesh_lighting_example` for an example using
