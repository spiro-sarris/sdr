from scipy.constants import speed_of_light
from rdfci import CorrelativeInterferometer

if __name__ == '__main__':

	# RF Frequency to measure and design the system unit = '[Hz == 1/s]
	rf_frequency = 900e6

	# Wavelength  Don't use variable name "lambda". reserved in Python language
	wavelength = speed_of_light / rf_frequency

	# Diamater of circle.  Design to be less than 1 wavelength so we don't
	# have to deal with integer multiples of 2	*pi (for now)
	diameter = 0.90 * wavelength

	# Number of angle steps to prepare in reference data set
	K = 360

	# List of number of antenna elements to process and compare results
	M_list = [3, 5, 7, 9, 11]

	# Print some debug before we start the simulation
	print('RF Frequency (f) [Hz]: {}'.format(rf_frequency))
	print('Wavelength (lambda) [m]: {}'.format(wavelength))
	print('Diameter of circle (diameter) [m]: {}'.format(diameter))
	print('Number of angles of arrival to simulate ref data set: {}'.format(K))
	print('Number of antenna elements to simulate {}'.format(M_list))

	# Create a correlative interferometer object
	ci =  CorrelativeInterferometer(wavelength, diameter, M_list, K, verbose=True)

	# Choose an angle to simulate an "unknown" arrival signal. unit = [degree]
	# It does not need to exactly match an angle in the reference data set.
	# the cost function algorithm finds the nearest match.
	AoA_deg = 120.6
	
	# Process one angle of arrival and generate a plot that shows the result
	# from a list of antenna configurations.
	ci.process_one(AoA_deg)
