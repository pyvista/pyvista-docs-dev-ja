# Download the dataset, split the bodies, and color each one.
#
import numpy as np
from pyvista import examples
dataset = examples.download_gears()
bodies = dataset.split_bodies()
for i, body in enumerate(bodies):  # pragma: no cover
    bid = np.empty(body.n_points)
    bid[:] = i
    body.point_data['Body ID'] = bid
bodies.plot(cmap='jet')
#
# .. seealso::
#
#     :ref:`Gears Dataset <gears_dataset>`
