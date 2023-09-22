from pyvista import examples
dataset = examples.download_st_helens()
dataset.plot(cmap="gist_earth")
#
# This dataset is used in the following examples:
#
# * :ref:`colormap_example`
# * :ref:`lighting_properties_example`
# * :ref:`plot_opacity_example`
# * :ref:`orbiting_example`
# * :ref:`plot_over_line_example`
# * :ref:`plotter_lighting_example`
