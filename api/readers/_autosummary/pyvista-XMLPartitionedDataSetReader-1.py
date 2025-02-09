import pyvista as pv
partitions = pv.PartitionedDataSet(
    [
        pv.Wavelet(extent=(0, 10, 0, 10, 0, 5)),
        pv.Wavelet(extent=(0, 10, 0, 10, 5, 10)),
    ]
)
partitions.save('my_partitions.vtpd')
_ = pv.read('my_partitions.vtpd')
