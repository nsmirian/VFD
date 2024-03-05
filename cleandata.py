
import time
#import pydoocs
import numpy as np
import matplotlib.pyplot as plt
import h5py


f=h5py.File('02272024104706.hdf5', 'r+')

#bamdBC1=f['bams/bamdBC1']
print(f['bams/bamdBC2'].shape)
print(f['bams/bamdBC1'].shape)
print(f['bams/bamuBC2'].shape)
print(f['bams/bamuBC1'].shape)
print(f['bams/bamuseed5'].shape)

print(f['compresor1/com11'].shape)
print(f['compresor1/com12'].shape)
print(f['compressor2/com21'].shape)
print(f['compressor2/com22'].shape)
print(f['compressor5/com52'].shape)
print(f['compressor5/com51'].shape)
#nonzeroindx=np.nonzero(bamuBC1[:,1,2])

#print(nonzeroindx[0][-1])

#bamuBC1=bamuBC1[nonzeroindx[0][-1],:,:]
#data[...] = X1 
#bamdBC1=f['bams/bamdBC1'][np.nonzero(bamdBC1[:,1,2])[0][-1],:,:]
#print(bamdBC1.shape)

bamdBC1=f['bams/bamdBC1'][np.nonzero(f['bams/bamdBC1'][:,1,2])[0][-1],:,:]
bamuBC1=f['bams/bamuBC1'][np.nonzero(f['bams/bamuBC1'][:,1,2])[0][-1],:,:]
bamdBC2=f['bams/bamdBC2'][np.nonzero(f['bams/bamdBC2'][:,1,2])[0][-1],:,:]
bamuBC2=f['bams/bamuBC2'][np.nonzero(f['bams/bamuBC2'][:,1,2])[0][-1],:,:]
bamuseed5=f['bams/bamuseed5'][np.nonzero(f['bams/bamuseed5'][:,1,2])[0][-1],:,:]

com11=f['compresor1/com11'][np.nonzero(f['compresor1/com11'][:,1,2])[0][-1],:,:]
com12=f['compresor1/com12'][np.nonzero(f['compresor1/com12'][:,1,2])[0][-1],:,:]
com21=f['compressor2/com21'][np.nonzero(f['compressor2/com21'][:,1,2])[0][-1],:,:]
com22=f['compressor2/com22'][np.nonzero(f['compressor2/com22'][:,1,2])[0][-1],:,:]
com51=f['compressor5/com51'][np.nonzero(f['compressor5/com51'][:,1,2])[0][-1],:,:]
com52=f['compressor5/com52'][np.nonzero(f['compressor5/com52'][:,1,2])[0][-1],:,:]


del f['bams/bamdBC1']
dset = f.create_dataset('bams/bamdBC1', data=bamdBC1)

del f['bams/bamdBC2']
dset = f.create_dataset('bams/bamdBC2', data=bamdBC2)

del f['bams/bamuBC1']
dset = f.create_dataset('bams/bamuBC1', data=bamuBC1)

del f['bams/bamuBC2']
dset = f.create_dataset('bams/bamuBC2', data=bamuBC2)

del f['bams/bamuseed5']
dset = f.create_dataset('bams/bamuseed5', data=bamuseed5)




del f['compresor1/com11']
dset = f.create_dataset('compresor1/com11', data=com11)

del f['compresor1/com12']
dset = f.create_dataset('compresor1/com12', data=com12)

del f['compressor2/com21']
dset = f.create_dataset('compressor2/com21', data=com21)

del f['compressor2/com22']
dset = f.create_dataset('compressor2/com22', data=com22)

del f['compressor5/com51']
dset = f.create_dataset('compressor5/com51', data=com51)

del f['compressor5/com52']
dset = f.create_dataset('compressor5/com52', data=com52)


#print(f['bams/bamdBC1'].shape)


#plt.plot( f['bams/bamdBC2'][1,:],'.' )
#plt.plot( f['bams/bamdBC1'][1,:],'.')
#plt.show()
f.close()


f=h5py.File('02272024104706.hdf5', 'r')
print(f['bams/bamdBC2'].shape)
print(f['bams/bamdBC1'].shape)
print(f['bams/bamuBC2'].shape)
print(f['bams/bamuBC1'].shape)
print(f['bams/bamuseed5'].shape)

print(f['compresor1/com11'].shape)
print(f['compresor1/com12'].shape)
print(f['compressor2/com21'].shape)
print(f['compressor2/com22'].shape)
print(f['compressor5/com52'].shape)
print(f['compressor5/com51'].shape)
f.close()

