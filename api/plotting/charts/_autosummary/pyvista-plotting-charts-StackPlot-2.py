import pyvista as pv
import numpy as np
year = [f'{y}' for y in np.arange(2011, 2021)]
x = np.arange(len(year))
n_e = [1739, 4925, 9515, 21727, 31452, 29926, 40648, 57761, 76370, 93702]
n_h = [5563, 7642, 11937, 13905, 22807, 46700, 60875, 53689, 46650, 50321]
n_f = [
    166556,
    157249,
    151552,
    138183,
    129669,
    113985,
    92965,
    73683,
    57097,
    29499,
]
chart = pv.Chart2D()
plot = chart.stack(x, [n_e, n_h, n_f])
plot.labels = ['Electric', 'Hybrid', 'Fossil']
chart.x_axis.label = 'Year'
chart.x_axis.tick_locations = x
chart.x_axis.tick_labels = year
chart.y_axis.label = 'New car sales'
chart.show()
