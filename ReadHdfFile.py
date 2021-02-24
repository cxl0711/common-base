from  __future__ import division
from pyhdf.SD import SD,SDC

import matplotlib.pyplot as plt
import pprint 

import sys

hdf_name = '/Users/cxl/Downloads/MOD15A2H.A2016001.h23v04.006.2016011194534.hdf'
print ('file found {}'.format(hdf_name)) 

hdf_obj = SD(hdf_name)
print (hdf_obj.info()) 

data_dic = hdf_obj.datasets()
for idx,sds in enumerate(data_dic.keys()):
	print (idx,sds)

for i in data_dic:
    print(i) 
    img = hdf_obj.select(i)[:]
    plt.imshow(img, cmap='gray')
    plt.show()
