# Download the aero bracket.
#
from pyvista import examples
dataset = examples.download_aero_bracket()
dataset
# Expected:
## UnstructuredGrid (...)
##   N Cells:    117292
##   N Points:   187037
##   X Bounds:   -6.858e-03, 1.118e-01
##   Y Bounds:   -1.237e-02, 6.634e-02
##   Z Bounds:   -1.638e-02, 1.638e-02
##   N Arrays:   3
#
# Show the available point data arrays.
#
dataset.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : None
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     displacement            float32    (187037, 3)
##     total nonlinear strain  float32    (187037, 6)
##     von Mises stress        float32    (187037,)
#
# Plot the von Mises stress.
#
cpos = [
    (-0.0503, 0.132, -0.179),
    (0.0505, 0.0185, -0.00201),
    (0.275, 0.872, 0.405),
]
dataset.plot(
    smooth_shading=True,
    split_sharp_edges=True,
    scalars='von Mises stress',
    cmap='bwr',
    cpos=cpos,
    anti_aliasing='fxaa',
)
#
# .. seealso::
#
#     :ref:`Aero Bracket Dataset <aero_bracket_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Notch Stress Dataset <notch_stress_dataset>`
#
#     :ref:`Notch Displacement Dataset <notch_displacement_dataset>`
#
#     :ref:`Fea Bracket Dataset <fea_bracket_dataset>`
