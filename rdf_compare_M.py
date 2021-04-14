import numpy as np
import matplotlib

# Set Matplotlib to use Qt5 for graphics (not default TKinter)
matplotlib.use("QT5agg")

import matplotlib.pyplot as plt
#plt.style.use('dark_background')

# Import for low level control of animation objects
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import (
			FigureCanvasQTAgg as FigureCanvas,
			NavigationToolbar2QT as NavigationToolbar)
import matplotlib.animation as animation

# Speed of light. unit = [m/s]
speed_of_light = 299792458

# RF Frequency to measure and design the system unit = '[Hz == 1/s]
freq = 900e6

# Wavelength  Don't use variable name "lambda". reserved in Python language
wavelength = speed_of_light / freq

# Wave number (spatial frequency) unit = [rad / m]
spatial_frequency = 2 * np.pi * freq / speed_of_light

# Diamater of circle.  Design to be less than 1 wavelength so we don't
# have to deal with integer multiples of 2	*pi (for now)
D = 0.90 * wavelength

# Radius of circle
R = D/2

print('RF Frequency (f) [Hz]: {}'.format(freq))
print('Wavelength (lambda) [m]: {}'.format(wavelength))
print('Spatial Frequency (k) [rad / m]: {}'.format(spatial_frequency))
print('Diameter of circle (D) [m]: {}'.format(D))
print('Radius of circle (R) [m]: {}'.format(R))

# Number of angle steps to record in reference data set
K = 360

# Number of antenna elements
M_list = [3, 5, 7, 9, 11]

# Configure graphs
figure_id = 'Angle of Arrival Simulation'
fig = plt.figure(figure_id, figsize=(8,6))
ax1a = fig.add_subplot(1, 1, 1)
ax1a.set_title("Correlative Interferometry Angle of Arrival")
ax1a.grid(True, which="both")
ax1a.set_xlabel('Angle')
ax1a.set_ylabel('Cost Function Result')

# Loop through the number of antenna elements and plot results as we go.
for M in M_list:
	# Indices of antenna elements. from 0 to M-1
	m = np.arange(M)

	# Angles at which we find the M antenna elements
	theta_m = (m / M) * 2 * np.pi

	# Angle of arrival of test signal [unit = rad]
	theta_k = np.linspace(0, 2 * np.pi, K, endpoint=False)

	# relative angles betwen all combinations of  Angle of Arrival theta_k 
	# and all antennas theta_m.  Result is a 2D array of size (K,M).  I want
	# the last dimension to be M because that is the dimension on which we
	# perform the correlation.

	# First, tile the arrays and broadcast to a 2D array so we can subract 
	# using 1 vector operation and not for loop
	theta_m_broadcast2D = np.tile(theta_m, (K,1))

	# Note the .T is transpose to prepare the dimensions to be (K, M)
	theta_k_broadcast2D = np.tile(theta_k, (M,1)).T 

	# Distance from center of circle to wavefront perpendicular to angle of arrival.
	# Depending on the relative angles theta_k and theta_m, some lenghts appear negative
	# a negative length doesn't have physical meaning, but the math is still valid because
	# these negative lengths result in valid phase difference values between -pi and 0.
	# Also remember that cos(-x) == cos(x).  So we will find the same result if we
	# subtrat (theta_m - theta_k) or (theta_k - theta_m).
	path_length_k_m_center = R * np.cos(theta_k_broadcast2D - theta_m_broadcast2D)

	# broadcast the path length of antenna 0 for all angles k into a 2D array
	# of size (K, M) to use vector operation and not for loop.
	path_length_0_k_broadcast2D = np.tile(path_length_k_m_center[:,0], (M, 1)).T

	# Relative distance between each antenna m and antenna 0 in the direction of
	# the traveling wave from angle of arrival theta_k
	path_length_k_m_ant0 = path_length_k_m_center - path_length_0_k_broadcast2D

	# Relative phase between antenna m and antenna 0.  From fraction of wavelength
	phase_difference_k_m_ant0 = 2 * np.pi * (path_length_k_m_ant0 / wavelength)

	# Numpy convolve and correlate functions only allow 1D input arrays.  Therefore
	# We must use a loop where we correlate the measurement phase data with the reference
	# phase data for each angle of arrival k.  Plot the result.

	# For now, take a slice of the simulated reference data and call this "measured data" 
	# Then we should have no problem to find a strong correlation peak at the correct
	# location in the reference data set.
	phase_m_measured = phase_difference_k_m_ant0[100,:]
	phase_m_measured_broadcast2D = np.tile(phase_m_measured,(K,1))

	# Cost function from the paper.
	# At first I tried using np.correlate as a cost function instead of np.sum(np.cos()).
	# It works most of the time, but sometimes the result is off by 1 or 2 angle indices.
	cost_function_result_k = np.sum(np.cos(phase_m_measured_broadcast2D - phase_difference_k_m_ant0), axis=1)

	maxpeak = np.max(cost_function_result_k)
	maxindex = np.where(cost_function_result_k == maxpeak)[0]
	maxangle = theta_k[maxindex]

	print('Number of antenna elements (M) [integer]: {}'.format(M))
	print('Indices of antennas: {}'.format(m))
	print('Angle location of each antenna [deg]: {}'.format(theta_m * 180 / np.pi))
	#print('Angles in reference data set theta_k [deg]: {}'.format(theta_k * 180 / np.pi))
	#print('Path length from antenna_m to center of circle [m]: {}'.format(path_length_k_m_center))
	#print('Path length from antenna_0 to center broadcast2D: {}'.format(path_length_0_k_broadcast2D))
	#print('Path length from antenna_m to antenna_0 [m]: {}'.format(path_length_k_m_ant0))
	#print('Phase difference from antenna_m to antenna_0 [rad]: {}'.format(phase_difference_k_m_ant0))
	#print('Measured phase data at each antenna relative to ant0 [rad] {}'.format(phase_m_measured))
	print('(Cost Function Value, Index, Angle) of highest correlation peak ({}, {}, {})'.format(maxpeak, maxindex, maxangle * 180 / np.pi))

	ax1a.plot(theta_k * 180 / np.pi, cost_function_result_k, '-+', label='M={}'.format(M))
	#ax1a.plot(theta_k * 180 / np.pi, cost_function_result_k, '+')

# After all lines are added to the graph in a loop, show the plot window once.
# If we show the plot window in the loop, it will block program execution
# until the user closes the window.
plt.legend()
plt.show()