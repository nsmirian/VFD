

# Collect data for compressions and BAMs
# First step of VFD project,
# Najmeh Mitian 23 feb 2024


import channels as addr
import time
import numpy as np
import pydoocs
import matplotlib.pyplot as plt
import h5py
#from datetime import date
from datetime import datetime

######################################## preperation of vectors
nshot=3000
timespam = datetime.now()
date_time = timespam.strftime("%m%d%Y%H%M%S")

filename=(date_time+'.hdf5')

charge_7FL2XTDS=np.zeros([nshot])
charge_timestamp=np.zeros([nshot])
charge_gun3=np.zeros([nshot])
charge_gun3e_timestamp=np.zeros([nshot])
###
x=np.zeros([nshot])
y=np.zeros([nshot])
x_timestamp=np.zeros([nshot])
y_timestamp=np.zeros([nshot])
XGM_energy=np.zeros([nshot])
XGM_timestamp=np.zeros([nshot])
bmenergyXTDS=np.zeros([nshot])
bmenergyXTDS_timestamp=np.zeros([nshot])
bmenergyFL2EXTR=np.zeros([nshot])
bmenergyFL2EXTR_timestamp=np.zeros([nshot])
###################################### compression data
#11
com11=pydoocs.read(addr.compressionTD11)
a,b=com11['data'].shape
com11=np.zeros([a,b,nshot])
com11_timestamp=np.zeros([nshot])
#####12
com12=pydoocs.read(addr.compressionTD12)
a,b=com12['data'].shape
com12=np.zeros([a,b,nshot])
com12_timestamp=np.zeros([nshot])
#####21
#com21=pydoocs.read(addr.compressionTD21)
#a,b=com21['data'].shape
com21=np.zeros([a,b,nshot])
com21_timestamp=np.zeros([nshot])
##22
#com22=pydoocs.read(addr.compressionTD22)
#com22_timestamp==np.zeros([nshot])
#a,b=com22['data'].shape
com22=np.zeros([a,b,nshot])
com22_timestamp=np.zeros([nshot])
###51
com51=pydoocs.read(addr.compressionTD51)
a,b=com51['data'].shape
com51=np.zeros([a,b,nshot])
com51_timestamp=np.zeros([nshot])
##52 ===> 6
com52=pydoocs.read(addr.compressionTD52)
a,b=com52['data'].shape
com52=np.zeros([a,b,nshot])
com52_timestamp=np.zeros([nshot])
#
######################################### BAM data
#1 ARRIVAL_TIME BC1
bamuBC1=pydoocs.read(addr.BAMUBC1)
a,b=bamuBC1['data'].shape
bamuBC1=np.zeros([a,b,nshot])
bamuBC1_timestamp=np.zeros([nshot])
#2 exit BC1
bamdBC1=pydoocs.read(addr.BAMDBC1)
a,b=bamdBC1['data'].shape
bamdBC1=np.zeros([a,b,nshot])
bamdBC1_timestamp=np.zeros([nshot])
###
#1 ARRIVAL_TIME BC2
bamuBC2=pydoocs.read(addr.BAMUBC2)
a,b=bamuBC2['data'].shape
bamuBC2=np.zeros([a,b,nshot])
bamuBC2_timestamp=np.zeros([nshot])
#2 exit   BC2
bamdBC1=pydoocs.read(addr.BAMDBC2)
a,b=bamdBC1['data'].shape
bamdBC2=np.zeros([a,b,nshot])
bamdBC2_timestamp=np.zeros([nshot])
##seed5 BAM
bamuseed5=pydoocs.read(addr.BAMseed5)
a,b=bamuseed5['data'].shape
bamuseed5=np.zeros([a,b,nshot])
bamuseed5_timestamp=np.zeros([nshot])

########################################## cammper , do not forget
cammeraT=pydoocs.read(addr.cam_data)
timestamp_img=np.zeros([nshot])
cam_img=np.zeros([640,2360,nshot])
cam_img_timestamp=np.zeros([nshot])
#############################################################################
############# data collection ############################################

for n in range(nshot):
    # compressions
    com11[:,:, n]     =pydoocs.read(addr.compressionTD11)['data']
    com11_timestamp[n]=pydoocs.read(addr.compressionTD11)['timestamp']
    com12[:,:, n]     =pydoocs.read(addr.compressionTD12)['data']
    com12_timestamp[n]=pydoocs.read(addr.compressionTD12)['timestamp']
    #com21[:,:, n]    =pydoocs.read(compressionTD21)['data']
    #com21_timestamp[n]=pydoocs.read(compressionTD21)['timestamp']
    #com22[:,:, n]     =pydoocs.read(compressionTD22)['data']
    #com22_timestamp[n]=pydoocs.read(compressionTD22)['timestamp']
    com51[:,:, n]     =pydoocs.read(addr.compressionTD51)['data']
    com51_timestamp[n]=pydoocs.read(addr.compressionTD51)['timestamp']
    com52[:,:, n]     =pydoocs.read(addr.compressionTD52)['data']
    com52_timestamp[n]=pydoocs.read(addr.compressionTD52)['timestamp']
    # BAMs
    bamuBC1[:,:, n]       =pydoocs.read(addr.BAMUBC1)['data']
    bamuBC1_timestamp[n]  =pydoocs.read(addr.BAMUBC1)['timestamp']
    bamDBC1[:,:, n]       =pydoocs.read(addr.BAMDBC1)['data']
    bamDBC1_timestamp[n]  =pydoocs.read(addr.BAMDBC1)['timestamp']
    bamuBC2[:,:, n]       =pydoocs.read(addr.BAMUBC2)['data']
    bamuBC2_timestamp[n]  =pydoocs.read(addr.BAMUBC2)['timestamp']
    bamdBC2[:,:, n]       =pydoocs.read(addr.BAMDBC2)['data']
    bamdBC2_timestamp[n]  =pydoocs.read(addr.BAMDBC2)['timestamp']
    bamuseed5[:,:, n]     =pydoocs.read(addr.BAMseed5)['data']
    bamuseed5_timestamp[n]=pydoocs.read(addr.BAMseed5)['timestamp']
    #camera
    cam_img[:,:, n]=pydoocs.read(addr.cam_data)['data']
    cam_img_timestamp[n]=pydoocs.read(addr.cam_data)['timestamp']
    # charge
    charge_7FL2XTDS[n]=pydoocs.read( addr.Charge7FL2XTDS)['data']
    charge_timestamp[n]=pydoocs.read(addr.Chage7FL2XTDS)['timestamp']
    charge_gun3[n]=pydoocs.read( addr.Chargegun3)['data']
    charge_gun3_timestamp[n]=pydoocs.read(addr.Chargegun3)['timestamp']
    # XTDS BPMs
    x[n]=pydoocs.read( addr.XTDSbpmx)['data']
    x_timestamp[n]=pydoocs.read(addr.XTDSbpmy)['timestamp']
    y[n]=pydoocs.read( addr.XTDSbpmy)['data']
    y_timestamp[n]=pydoocs.read(addr.XTDSbpmy)['timestamp']


    bmenergyXTDS[n]=pydoocs.read( addr.beamenergyXTDS)['data']
    bmenergyXTDS_timestamp[n]=pydoocs.read( addr.beamenergyXTDS)['timestamp']

    bmenergyFL2EXTR[n]=pydoocs.read( addr.beamenergyFL2EXTR)['data']
    bmenergyFL2EXTR_timestamp[n]=pydoocs.read( addr.beamenergyFL2EXTR)['timestamp']

    XGM_energy[n]=pydoocs.read( addr.XGM_DP)['data']
    XGM_timestamp[n]=pydoocs.read( addr.XGM_DP)['timestamp']

    time.sleep( 0.1 )
    print(n)


####################################################
####################################################

data_dict = {
    'compresor1': {
        'com11': com11,
        'com12': com12,
        'com11_timestamp': com11_timestamp,
        'com12_timestamp': com12_timestamp
        },
    'compressor2': {
        'com21': com21,
        'com22': com22,
        'com21_timestamp': com21_timestamp,
        'com22_timestamp': com22_timestamp
        },
    'compressor5': {
        'com51': com51,
        'com52': com52,
        'com51_timestamp': com51_timestamp,
        'com52_timestamp': com52_timestamp
        },
     'bams': {
        'bamuBC1': bamuBC1,
        'bamdBC1': bamdBC1,
        'bamdBC1_timestamp': bamdBC1_timestamp,
        'bamuBC1_timestamp': bamuBC1_timestamp,
        'bamuBC2': bamuBC2,
        'bamdBC2': bamdBC2,
        'bamdBC2_timestamp': bamdBC2_timestamp,
        'bamuBC2_timestamp': bamuBC2_timestamp,
        'bamuseed5': bamuseed5,
        'bamuseed5_timestamp': bamuseed5_timestamp

        },
    'camera_image': {
        'cam_img': cam_img,
        'cam_img_timestamp': cam_img_timestamp,
        },
	'bpm'   : {
    	'x':x,
    	'x_timestamp':x_timestamp,
    	'y': y,
    	'y_timestamp':y_timestamp
    	},
	'charge':{
		'charge_FE2':charge_7FL2XTDS,
		'charge_timestamp':charge_timestamp},

    'beam_energy':{'beamenergyXTDS':bmenergyXTDS,
        'beamenergyXTDS_timestamp':  bmenergyXTDS_timestamp,
        'beamenergyFL2EXTR':bmenergyFL2EXTR,
        'beamenergyFL2EXTR_timestamp':bmenergyFL2EXTR_timestamp} ,

    'XGM':{'XGM_energy':XGM_energy, 'XGM_timestamp':  XGM_timestamp}

}


#######################################################################
##### Open HDF5 file and write in the data_dict structure and info
f = h5py.File(filename, 'w')
for grp_name in data_dict:
    grp = f.create_group(grp_name)
    for dset_name in data_dict[grp_name]:
        dset = grp.create_dataset(dset_name, data = data_dict[grp_name][dset_name])
       # print(grp_name, dset_name, data_dict[grp_name][dset_name])
f.close()
