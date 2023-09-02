#!/usr/bin/env python3

from datetime import datetime
from scipy.io import wavfile
import numpy as np
import os
import subprocess

offset_dbspl = 75 # Adjust this value for accuracy.

while True:
	# Record 1 second.
	subprocess.run(["arecord", "-d", "1", "-f", "S16_LE", "-c", "1", "-r", "48000", "/tmp/8a32ada4c3e0c1f0.bin"])

	# Calculate average [dBSPL]
	sample_rate, data = wavfile.read("/tmp/8a32ada4c3e0c1f0.bin") # Read recording.
	rms = np.sqrt(np.mean(np.square(data.astype(np.float64)))) # Calculate RMS.
	ref_pressure = 20.0e-6 # Set reference sound pressure (20 uPa)
	dbspl = 20 * np.log10(rms / ref_pressure) # Calculate "dBSPL"
	dbspl_adjusted = dbspl - offset_dbspl # Apply Offset to "dBSPL"

	# Write out calculated value
	current_time = datetime.now().isoformat()
	with open("/tmp/8a32ada4c3e0c1f0.csv", "w") as f:
		f.write(f"{current_time}\t{dbspl_adjusted:.2f}\tdBSPL\n")
