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


###############################
#Einlesen Daten


fname='Aufg3mit.dat'
ncols=2
data_array, info_dict =\
  readColumnData(fname, ncols, delimiter=' ', pr=False)

# print what we got:
freq=data_array[:,0] # 1st column
nutfreq=data_array[:,1] # 2nd column


xdata=freq
ydata=nutfreq
yerror=0.00000


####################
# Helper functions #
####################

def generate_datasets(output_file_path):
    '''The following block generates the Datasets and writes a file for
    each of them.'''

    import numpy as np  # need some functions from numpy
    
    my_datasets = []
    my_datasets.append(kafe.Dataset(data=(xdata, ydata)))
    my_datasets[-1].add_error_source('y', 'simple', yerror)
    
    my_datasets[0].write_formatted(output_file_path)


############
# Workflow #
############

# Generate the Dataset and store it in a file
generate_datasets('Aufg3mitk.dat')

# Initialize Dataset
my_datasets = [kafe.Dataset(title="Nutationsfrequenz")]
# Load the Dataset from the file
my_datasets[0].read_from_file(input_file='Aufg3mitk.dat')


# Create the Fits

my_fits = [kafe.Fit(dataset,linear_2par,
                    fit_label="Linear regression ")
           for dataset in my_datasets]
# Do the Fits
for fit in my_fits:
    fit.do_fit()

# Create the plots
my_plot = kafe.Plot(my_fits[0])#,my_fits[1])



#Verschoenern
my_plot.axis_labels = ['$Frequenz$ (1/s)', '$Nutationsfrequenz$ (1/s)']

# Draw the plots
my_plot.plot_all()  # only show data once (it's the same data)

###############
# Plot output #
###############

# Save the plots
my_plot.save('Aufg3mitk.pdf')

'''
# check contours
contour1 = my_fits[0].plot_contour(0, 1, dchi2=[1.,2.3])
profile00=my_fits[0].plot_profile(0)
profile01=my_fits[0].plot_profile(1)
contour2 = my_fits[1].plot_contour(0, 1, dchi2=[1.,2.3])
'''
#contour1.savefig('kafe_example1_contour1.pdf')
#contour2.savefig('kafe_example1_contour2.pdf')
#profile00.savefig('kafe_example1_profile00.pdf')
#profile01.savefig('kafe_example1_profile01.pdf')

# Show the plots
#my_plot.show()
