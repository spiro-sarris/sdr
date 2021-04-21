import numpy as np
from scipy.constants import speed_of_light

import matplotlib
from matplotlib.lines import Line2D

# Set Matplotlib to use Qt5 for graphics (not default TKinter)
matplotlib.use("QT5agg")
import matplotlib.pyplot as plt
plt.style.use('dark_background')

class MeasuredDataSimulator:
	def __init__(self, wavelength, diameter, M_antennas_list, angle_of_arrival, verbose=True):
		'''
		Class to simulate measured phase data from all antennas in the array for 1
		angle of arrival.  Phase data is relative to antenna element 0.  
		For simulation, we must choose this angle.  For actual measurement, 
		we calcualte the phase difference using complex divide operator .

		Parameters
		----------
		wavelength : wavelength of rf signal to simulate

		diameter ; diamter of circle antenna array. unit = [m]

		M_antennas_list : list of number of antennas in the array.  Must be odd number >= 3

		angle_of_arrival : angle of arrival to simulate received phase. unit = [deg]
		'''

		radius = diameter / 2

		# Create an empty dictionary to append "measured" data
		# Keep in member variables and use again outside
		self.phase_difference_m_ant0 = {}

		# Loop through the antenna configurations in M_antennas_list and
		# append to the dictionary of measured data sets.
		# the first key of the dictionary is the integer number of antenna elements M
		for M_antennas in M_antennas_list:
			# Indices of antenna elements. from 0 to M-1
			m = np.arange(M_antennas)

			# Angles at which we find the M antenna elements
			theta_m = (m / M_antennas) * 2 * np.pi

			# Create a new variable named theta_k to make code look consistent with
			# ReferenceDataSimulator
			self.theta_k = angle_of_arrival

			# relative angles betwen Angle of Arrival theta_k
			# and all antennas theta_m.  Result is a 1D array of size (1,M).  I want
			# the last dimension to be M because that is the dimension on which we
			# perform the correlation / cost function.

			# Broadcast the single value of theta_k to a numpy array with
			# dimensions (1, M).  Use for numpy vectorized operations.
			theta_k_broadcast1D = np.tile(self.theta_k, M_antennas) 

			# Distance from center of circle to wavefront perpendicular to angle of arrival.
			# Depending on the relative angles theta_k and theta_m, some lenghts appear negative
			# a negative length doesn't have physical meaning, but the math is still valid because
			# these negative lengths result in valid phase difference values between -pi and 0.
			# Also remember that cos(-x) == cos(x).  So we will find the same result if we
			# subtrat (theta_m - theta_k) or (theta_k - theta_m).
			path_length_m_center = radius * np.cos(theta_k_broadcast1D - theta_m)

			# Relative distance between each antenna m and antenna 0 in the direction of
			# the traveling wave from angle of arrival theta_k
			path_length_m_ant0 = path_length_m_center - path_length_m_center[0]

			# Relative phase between antenna m and antenna 0.  From fraction of wavelength
			# Save this result to the dictionary of reference data sets indexed by key
			# M_antennas.
			self.phase_difference_m_ant0[M_antennas] = 2 * np.pi * (path_length_m_ant0 / wavelength)

			if(verbose is True):
				print('----------------------')
				print('MeasuredDataSimulator')
				print('----------------------')
				print('Number of antenna elements (M_antennas) [integer]: {}'.format(M_antennas))
				print('Indices of antennas: {}'.format(m))
				print('Angle location of each antenna [deg]: {}'.format(np.degrees(theta_m)))
				print('Angle of Arrival theta_k [deg]: {}'.format(np.degrees(self.theta_k)))
				print('Path length from antenna_m to center of circle [m]: {}'.format(path_length_m_center))
				print('Path length from antenna_m to antenna_0 [m]: {}'.format(path_length_m_ant0))
				print('Phase difference from antenna_m to antenna_0 [rad]: {}'.format(self.phase_difference_m_ant0[M_antennas]))

class ReferenceDataSimulator:
	def __init__(self, wavelength, diameter, M_antennas_list, K_angles, verbose=True):
		''''
		Class to simulate the reference data set.  Includes phase differences
		from all antennas relative to antenna 0.  Angle range is always 360 degrees. 
		n_angles data points are linearly spaced between 0 and 360(1-1/n_angles).
		The last angle in the data set is 1 angle resulution point less than 360 
		degrees to avoid ambiguity with 0.

		Parameters
		----------
		wavelength : wavelength of rf signal to simulate

		diameter ; diamter of circle antenna array. unit = [m]

		M_antennas : number of antennas in the array.  Must be odd number >= 3

		K_angles : number of AoA angles to simulate in the reference data set.
		'''
		
		radius = diameter / 2

		# Angles of arrival to simulate in reference data set [unit = rad]
		# endpoint= False to avoid ambiguous angles 0 and 360.
		self.theta_k = np.linspace(0, 2 * np.pi, K_angles, endpoint=False)

		# Create an empty dictionary to append reference data sets
		# Keep these as member variables so we can use from outside after.
		self.phase_difference_k_m_ant0 = {}
		self.theta_m_dict = {}

		# Loop through the antenna configurations in M_antennas_list and
		# append to the dictionary of reference data sets.
		# the first key of the dictionary is the integer number of antenna elements M
		for M_antennas in M_antennas_list:
			# Indices of antenna elements. from 0 to M-1
			m = np.arange(M_antennas)

			# Angles at which we find the M antenna elements
			self.theta_m_dict[M_antennas] = (m / M_antennas) * 2 * np.pi

			# relative angles betwen all combinations of  Angle of Arrival theta_k 
			# and all antennas theta_m.  Result is a 2D array of size (K,M).  I want
			# the last dimension to be M because that is the dimension on which we
			# perform the correlation / cost function.

			# First, tile the arrays and broadcast to a 2D array so we can subract 
			# using 1 vector operation and iterate loops
			theta_m_broadcast2D = np.tile(self.theta_m_dict[M_antennas], (K_angles,1))

			# Note the .T is transpose to prepare the dimensions to be (K, M)
			theta_k_broadcast2D = np.tile(self.theta_k, (M_antennas,1)).T 

			# Distance from center of circle to wavefront perpendicular to angle of arrival.
			# Depending on the relative angles theta_k and theta_m, some lenghts appear negative
			# a negative length doesn't have physical meaning, but the math is still valid because
			# these negative lengths result in valid phase difference values between -pi and 0.
			# Also remember that cos(-x) == cos(x).  So we will find the same result if we
			# subtrat (theta_m - theta_k) or (theta_k - theta_m).
			path_length_k_m_center = radius * np.cos(theta_k_broadcast2D - theta_m_broadcast2D)

			# broadcast the path length of antenna 0 for all angles k into a 2D array
			# of size (K, M) to use vector operation and not loop.
			path_length_0_k_broadcast2D = np.tile(path_length_k_m_center[:,0], (M_antennas, 1)).T

			# Relative distance between each antenna m and antenna 0 in the direction of
			# the traveling wave from angle of arrival theta_k
			path_length_k_m_ant0 = path_length_k_m_center - path_length_0_k_broadcast2D

			# Relative phase between antenna m and antenna 0.  From fraction of wavelength
			# Save this result to the dictionary of reference data sets indexed by key
			# M_antennas.
			self.phase_difference_k_m_ant0[M_antennas] = 2 * np.pi * (path_length_k_m_ant0 / wavelength)

			if(verbose is True):
				print('----------------------')
				print('ReferenceDataSimulator')
				print('----------------------')
				print('Number of antenna elements (M_antennas) [integer]: {}'.format(M_antennas))
				print('Indices of antennas: {}'.format(m))
				print('Angle location of each antenna [deg]: {}'.format(np.degrees(self.theta_m_dict[M_antennas])))
				print('Angles in reference data set theta_k [deg]: {}'.format(np.degrees(self.theta_k)))
				print('Path length from antenna_m to center of circle [m]: {}'.format(path_length_k_m_center))
				print('Path length from antenna_0 to center broadcast2D: {}'.format(path_length_0_k_broadcast2D))
				print('Path length from antenna_m to antenna_0 [m]: {}'.format(path_length_k_m_ant0))
				print('Phase difference from antenna_m to antenna_0 [rad]: {}'.format(self.phase_difference_k_m_ant0[M_antennas]))

class CorrelativeInterferometer:
	def __init__(self, wavelength, diameter, M_antennas_list, K, verbose=True):
		'''
		TODO: Docstring
		'''
		# Save the parameters to instance member variables for future use
		self.wavelength = wavelength
		self.diameter = diameter
		self.M_antennas_list = M_antennas_list
		self.K = K
		self.verbose = verbose

		# Simulate reference phase data for all configurations of M antennas.
		self.reference_data_simulator = ReferenceDataSimulator(wavelength, diameter, M_antennas_list, K, verbose)

		# Configure graphs
		self.figure_id = 'Correlative Interferometry Simulation'
		self.fig = plt.figure(self.figure_id, figsize=(12,8))
		self.gridspec = self.fig.add_gridspec(2, len(self.M_antennas_list))

		# Create this dictionary to keep Line2D objects and index by number of
		# antennas in the array configuration
		self.AoA_polar_axis_dict = {}

		# Loop through the antenna configurations in M_antennas_list and
		# Create a matplotlib axis object
		# the first key of the dictionary is the integer number of antenna elements M
		# Iterate through array indices rather than values of M_antennas_list 
		# because we need this index for the subplot function
		for M_antennas_list_index in np.arange(len(self.M_antennas_list)):
			# Add a new axis obaxisject to the dictionary
			M_antennas = self.M_antennas_list[M_antennas_list_index]
			self.AoA_polar_axis_dict[M_antennas] = self.fig.add_subplot(self.gridspec[0, M_antennas_list_index], projection='polar')
			#self.AoA_polar_axis_dict[M_antennas] = self.fig.add_subplot(2, len(self.M_antennas_list), M_antennas_list_index+1, projection='polar')
			self.AoA_polar_axis_dict[M_antennas].set_title('M={}'.format(M_antennas))
			self.AoA_polar_axis_dict[M_antennas].set_theta_zero_location('N')
			self.AoA_polar_axis_dict[M_antennas].set_theta_direction(-1)
			self.AoA_polar_axis_dict[M_antennas].grid(True, which="both", alpha=0.4)
			self.AoA_polar_axis_dict[M_antennas].set_rticks([])
			self.AoA_polar_axis_dict[M_antennas].set_rlim((0,1.1))

		self.ax2 = self.fig.add_subplot(self.gridspec[1, :])
		self.ax2.set_title("Correlation Cost Function")
		self.ax2.grid(True, which="both", alpha=0.4)
		self.ax2.set_xlabel('Azimuth Angle')
		self.ax2.set_ylabel('Cost Function Result')
		self.ax2.set_xlim((0,360))
		self.ax2.set_ylim((-5, 15))

		# Choose colors for the lines in the cost function graphs
		self.colors = {3 : 'yellow',
				5 : 'cyan',
				7 : 'magenta',
				9 : 'blue',
				11 : 'white'}

	def work(self, phase_m_measured):
		'''
		Cost function from the paper.
		Use the function name "work()" to more easily translate this python prototype into
		a GNURadio block which requires a work() function.
		At first I tried using np.correlate as a cost function instead of np.sum(np.cos()).
		It works most of the time, but sometimes the result is off by 1 or 2 angle indices.
		'''
		# Create empty dictionaries to append cost function results data sets
		cost_k = {}
		max_value = {}
		max_index = {}
		max_angle = {}

		# Loop through the antenna configurations in M_antennas_list and
		# append to the dictionary of cost function result sets.
		# the first key of the dictionary is the integer number of antenna elements M
		for M_antennas in self.M_antennas_list:
			phase_m_measured_broadcast2D = np.tile(phase_m_measured[M_antennas],(self.K,1))

			# Use the cost function to correlate measured data with reference data sets
			# Append resuts to dictionary according to key M_antennas configuration.
			cost_k[M_antennas] = np.sum(np.cos(phase_m_measured_broadcast2D - self.reference_data_simulator.phase_difference_k_m_ant0[M_antennas]), axis=1)

			# Find the maximum value of the cost function
			max_value[M_antennas] = np.max(cost_k[M_antennas])
			
			# Find the index of the maximum value  value of the cost function
			max_index[M_antennas] = np.where(cost_k[M_antennas] == max_value[M_antennas])[0]
			
			# Find the angle of arrival at this array index.
			max_angle[M_antennas] = self.reference_data_simulator.theta_k[max_index[M_antennas]]
			if(self.verbose is True):
				print('-------------------------')
				print('CorrelativeInterferometer')
				print('-------------------------')
				print('(Cost Function Value, Index, Angle) of highest correlation peak ({}, {}, {})'.format(max_value[M_antennas], max_index[M_antennas], np.degrees(max_angle[M_antennas])))

		# Return the complete dictionaries of results
		return(cost_k, max_value, max_angle)

	def process_one(self, AoA):
		'''
		Process one angle of arrival for all antenna configurations M_antennas_list.

		Parameters
		----------
		AoA : Angle of Arrival [deg]
		'''

		AoA_radian = np.radians(AoA)

		# Simulate measured data for the current ange AoA and all configuratinos of M antennas.
		measured_data_simulator = MeasuredDataSimulator(self.wavelength, self.diameter, self.M_antennas_list, AoA_radian, self.verbose)
		
		# Send measured data through the Correlator. Return values are all dictionaries
		# of results indexed by primary key antenna configuration M_antennas.
		(cost_k, max_value, max_angle) = self.work(measured_data_simulator.phase_difference_m_ant0)

		# Make some graphs
		for M_antennas in self.M_antennas_list:
			self.AoA_polar_axis_dict[M_antennas].plot(self.reference_data_simulator.theta_m_dict[M_antennas], np.ones(M_antennas), marker='.', linestyle='none', color=self.colors[M_antennas], markersize=8, label='antenna loc')
			self.AoA_polar_axis_dict[M_antennas].plot(AoA_radian, 1, marker='+', color='yellow', markersize=14, mew=2, label='input'.format(M_antennas))
			self.AoA_polar_axis_dict[M_antennas].plot(max_angle[M_antennas], 1, marker='+', color='blue', markersize=10, mew=1, label='output'.format(M_antennas))
			
			self.ax2.plot(np.degrees(self.reference_data_simulator.theta_k), cost_k[M_antennas], '-+', color=self.colors[M_antennas], label='M={}'.format(M_antennas))
			
		# After all lines are added to the graph in a loop, show the plot window once.
		# If we show the plot window in the loop, it will block program execution
		# until the user closes the window.
		self.AoA_polar_axis_dict[M_antennas].legend(bbox_to_anchor=(1.1,1.0), loc='upper left')
		self.ax2.legend(loc='upper right')
		plt.show()

	def process_animation(self):
		'''
		TODO
		'''

		# Create this dictionary to keep Line2D objects and index by number of
		# antennas in the array configuration
		self.AoA_polar_sim_line_dict = {}
		self.AoA_polar_result_line_dict = {}
		self.AoA_polar_antenna_loc_line_dict = {}
		self.cost_function_line_dict = {}

		for M_antennas in self.M_antennas_list:
			# Create Line2D object for AoA polar plot
			line_AoA_polar_sim = Line2D([0],[0], marker='+', color='yellow', markersize=24, mew=6, label='input'.format(M_antennas))
			line_AoA_polar_result = Line2D([0],[0], marker='+', color='blue', markersize=20, mew=3, label='output'.format(M_antennas))
			line_AoA_polar_antenna_loc = Line2D(self.reference_data_simulator.theta_m_dict[M_antennas], np.ones(M_antennas), marker='.', linestyle='none', color=self.colors[M_antennas], markersize=8, label='antenna loc')
			
			# Add the new Line2D object to the dictionary that we can access later for update
			self.AoA_polar_antenna_loc_line_dict[M_antennas] = line_AoA_polar_antenna_loc
			# Add the new Line2D object to the axis of the figure window.
			self.AoA_polar_axis_dict[M_antennas].add_line(line_AoA_polar_antenna_loc)

			# Add the new Line2D object to the dictionary that we can access later for update
			self.AoA_polar_sim_line_dict[M_antennas] = line_AoA_polar_sim
			# Add the new Line2D object to the axis of the figure window.
			self.AoA_polar_axis_dict[M_antennas].add_line(line_AoA_polar_sim)

			# Add the new Line2D object to the dictionary that we can access later for update
			self.AoA_polar_result_line_dict[M_antennas] = line_AoA_polar_result
			# Add the new Line2D object to the axis of the figure window.
			self.AoA_polar_axis_dict[M_antennas].add_line(line_AoA_polar_result)

			# Create Line2D objects for cost function results
			line_cost_function = Line2D([0],[0], color=self.colors[M_antennas], label='M={}'.format(M_antennas))
			# Add the new Line2D object to the dictionary that we can access later for update
			self.cost_function_line_dict[M_antennas] = line_cost_function
			# Add the new Line2D object to the axis of the figure window.
			self.ax2.add_line(line_cost_function)

		# Frame update rate
		frame_rate = 30
		update_interval_ms = 1000*(1/frame_rate)

		print('Start animation rate = {:.1f} frames per second'.format(frame_rate))
		self.ani_cost_function = matplotlib.animation.FuncAnimation(self.fig, self.update_plot_cost_function, frames=self.angle_generator, interval=update_interval_ms, blit=True, save_count=360)

		self.AoA_polar_axis_dict[M_antennas].legend(bbox_to_anchor=(1.1,1.0), loc="upper left")
		self.ax2.legend(loc='upper right')

		# ----------- Write animation to video file output -------------------------
		# Save an mp4 video of 360 frames (one full round) before we show the graph.
		# Create an object of that writer class.
		# Note ** This function appears "slow" because it takes a long time to convert
		# the matplotlib graphics into mp4.
		
		# --- uncomment these lines to write a .mp4 file ---------
		# filename = 'rdfci_simulation.mp4'
		# print('Saving the first 360 frames to {} ...'.format(filename))
		# writer = matplotlib.animation.FFMpegWriter(fps=frame_rate)
		# self.ani_cost_function.save(filename, writer)

		print('Close GUI window to exit ...')
		plt.show()


	def update_plot_cost_function(self, AoA_radian):
		'''
		Reference for how to do efficient real-time graph updates.  Combine the technique from these two:
		
		https://matplotlib.org/gallery/animation/strip_chart.html
		Oscilloscope example.  Use this method of constructing lines, append data, update lines.
		This example updates the graphics using matplotlib FuncAnimation
		
		https://stackoverflow.com/questions/11874767/how-do-i-plot-in-real-time-in-a-while-loop-using-matplotlib
		Another example of how to use blit() manually without FuncAnimation class.

		AoA_radian is the value yielded by the angle_generator function. Matplotlib FuncAnimation
		calls this generator function at the frame rate and passes the yield value to
		update_plot.
		'''

		# Simulate measured data for the current ange AoA and all configuratinos of M antennas.
		measured_data_simulator = MeasuredDataSimulator(self.wavelength, self.diameter, self.M_antennas_list, AoA_radian, self.verbose)
		
		# Send measured data through the Correlator. Return values are all dictionaries
		# of results indexed by primary key antenna configuration M_antennas.
		(cost_k, max_value, max_angle) = self.work(measured_data_simulator.phase_difference_m_ant0)
		for M_antennas in self.M_antennas_list:
			self.cost_function_line_dict[M_antennas].set_data(np.degrees(self.reference_data_simulator.theta_k), cost_k[M_antennas])
			self.AoA_polar_sim_line_dict[M_antennas].set_data(AoA_radian, 1)
			self.AoA_polar_result_line_dict[M_antennas].set_data(max_angle[M_antennas], 1)

		return(list(self.cost_function_line_dict.values()) + list(self.AoA_polar_sim_line_dict.values()) + list(self.AoA_polar_result_line_dict.values()))

	def angle_generator(self):
		AoA_all_radian = np.radians(np.arange(360))
		for AoA_radian in AoA_all_radian:
			yield AoA_radian
