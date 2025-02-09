from pyvista import examples
grid = examples.load_explicit_structured()
grid.plot(show_edges=True)
#
# .. seealso::
#
#     :ref:`Explicit Structured Dataset <explicit_structured_dataset>`
