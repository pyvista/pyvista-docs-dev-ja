# Create and plot a single triquadratic pyramid.
#
from pyvista import examples
grid = examples.cells.TriQuadraticPyramid()
examples.plot_cell(grid)
#
# List the grid's cells.
#
grid.cells
# Expected:
## array([19,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
##        16, 17, 18])
#
# List the grid's points.
#
grid.points
# Expected:
## pyvista_ndarray([[0.        , 0.        , 0.5       ],
##                  [1.        , 0.        , 0.5       ],
##                  [1.        , 1.        , 0.5       ],
##                  [0.        , 1.        , 0.5       ],
##                  [0.5       , 0.5       , 1.        ],
##                  [0.5       , 0.        , 0.5       ],
##                  [1.        , 0.5       , 0.5       ],
##                  [0.5       , 1.        , 0.5       ],
##                  [0.        , 0.5       , 0.5       ],
##                  [0.25      , 0.25      , 0.75      ],
##                  [0.75      , 0.25      , 0.75      ],
##                  [0.75      , 0.75      , 0.75      ],
##                  [0.25      , 0.75      , 0.75      ],
##                  [0.5       , 0.5       , 0.5       ],
##                  [0.5       , 0.16666667, 0.66666667],
##                  [0.83333333, 0.5       , 0.66666667],
##                  [0.5       , 0.83333333, 0.66666667],
##                  [0.16666667, 0.5       , 0.66666667],
##                  [0.5       , 0.5       , 0.625     ]])
#
grid.celltypes  # same as pyvista.CellType.TRIQUADRATIC_PYRAMID
# Expected:
## array([37], dtype=uint8)
