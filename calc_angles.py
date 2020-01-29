import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('dark_background')
matplotlib.use("QT5Agg")

# Constants
speed_of_light_m_per_s = 299792458

# Choose frequency
freq_hz = 433.0e6

# Choose angles
aoa_boresight = np.linspace(-90, 90, 181)
aoa_select = aoa_boresight - 90

# Derived parameters
wavelength_m = speed_of_light_m_per_s / freq_hz
spatial_frequency_rad_per_meter = 2*np.pi*freq_hz / speed_of_light_m_per_s
aoa_rad = aoa_select*np.pi/180.0

# Choose array spacing to be 1/2 of wavelength (to avoid phase ambiguity)
baseline_length_m = wavelength_m/2.0


# Print debug output
print("Speed of light [m]:\t\t\t%f" 				% speed_of_light_m_per_s)
print("RF frequency [MHz]:\t\t\t%f" 				% (freq_hz / 1e6))
print("Baseline Length [m]:\t\t\t%f"				% baseline_length_m)
print("Wavelength [m]:\t\t\t\t%f" 					% wavelength_m)
print("Spatial Freqency [radian/meter]:\t%f"	% spatial_frequency_rad_per_meter)

# Calculate phase difference
delta_phase = spatial_frequency_rad_per_meter * baseline_length_m * np.cos(aoa_rad)

# From phase difference, calculate angle of arrival
aoa_calc = np.arccos(delta_phase/(spatial_frequency_rad_per_meter*baseline_length_m))
aoa_calc_deg_boresight = aoa_calc*180/(np.pi) - 90
# Make plots

figure_size = (8,6)
fig1 = plt.figure('Beam Steering', figsize=figure_size)
ax1a = fig1.add_subplot(1,1,1)
ax1a.set_title('Beam Steering. f = %5.2f [MHz], D = %4.2f [m]' % (1e-6*freq_hz, baseline_length_m))
ax1a.plot(aoa_boresight, delta_phase)
#ax1a.set_xlim((aoa_boresight[0], aoa_boresight[-1]))
ax1a.set_xlabel('Select Beam Steer Angle [degs]')
ax1a.set_ylabel('Calcualte Phase Adust (Steering Vector) [rad]')
ax1a.grid(True, which='both')

figure_size = (8,6)
fig2 = plt.figure('Angle of Arrival', figsize=figure_size)
ax2a = fig2.add_subplot(1,1,1)
ax2a.set_title('Angle of Arrival. f = %5.2f [MHz], D = %4.2f [m]' % (1e-6*freq_hz, baseline_length_m))
ax2a.plot(delta_phase, aoa_calc_deg_boresight)
#ax2a.set_xlim((delta_phase[0], delta_phase[-1]))
ax2a.set_xlabel('Phase Difference [rad]')
ax2a.set_ylabel('Angle of Arrival [degs]')
ax2a.grid(True, which='both')



plt.show()