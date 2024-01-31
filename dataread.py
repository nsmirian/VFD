import time
#import pydoocs
import numpy as np
import matplotlib.pyplot as plt
import h5py

f=h5py.File('data_jan15_axisin_lasingoff400_lastpphase.hdf5', 'r')

print(f.keys())
print(f['1'].keys())
data1c11=f['1']['com11']
#data1c11.shape
nonzeroindx=np.nonzero(data1c11[:,1,2])
datacomp11=data1c11[nonzeroindx[0],1,:]
print(datacomp11.shape)
data1c12=f['1']['com12']
nonzeroindx=np.nonzero(data1c12[:,1,2])
datacomp12=data1c12[nonzeroindx[0],1,:]
print(datacomp12.shape)
data1c51=f['5']['com51']
nonzeroindx=np.nonzero(data1c51[:,1,2])
datacomp51=data1c51[nonzeroindx[0],1,:]
print(datacomp51.shape)
