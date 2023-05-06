# Create boxplots for datasets sampled from shifted normal distributions.
#
import pyvista
import numpy as np
rng = np.random.default_rng(1)  # Seeded random number generator used for data generation
normal_data = [rng.normal(i, size=50) for i in range(5)]
chart = pyvista.ChartBox(normal_data, labels=[f"x ~ N({i},1)" for i in range(5)])
chart.show()
