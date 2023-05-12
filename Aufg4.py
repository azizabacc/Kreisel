'''
Comparison of two models for the same data
------------------------------------------

    In this example, two models (exponential and linear) are fitted
to data from a single Dataset.
'''

###########
# Imports #
###########

# import everything we need from kafe
import kafe
# script test_readColumnData.py
# -*- coding: utf-8 -*-

import sys, numpy as np, matplotlib.pyplot as plt
from PhyPraKit import odFit, labxParser, readColumnData
# additionally, import the two model functions we
# want to fit:
from kafe.function_library import linear_2par, exp_2par



fname='Aufg4.dat'
ncols=7
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
x=data_array[:,0] # 1st column
rnull=data_array[:,1] # 2nd column





#plt.plot(x,rnull,'bs')
plt.plot(x,rnull,'k.', label='r=0cm')




#plt.axis([5,45,0,130])
#plt.grid()
plt.xlabel('Zeit t (s)',size='large')
plt.ylabel('Drehfrequenz f (1/s)',size='large')

plt.savefig('Aufg4.pdf')


plt.show()
