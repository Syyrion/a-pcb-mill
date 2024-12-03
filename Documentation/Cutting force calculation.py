# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:51:04 2024

@author: Azam1
"""

import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate cutting force
def calculate_cutting_force(S, n, D, CL, d, us):
    # Feed rate (F) calculation
    F = S * CL * n  # in mm/min
    
    # Material Removal Rate (MRR)
    MRR = F * D * d / 1000  # Convert mm^3/min to mm^3/s
    
    # Power requirement (P)
    P = us * MRR  # in Watts
    
    # Cutting force (Fc) calculation
    Fc = P / (S * np.pi * (D / 1000) / 60)  # Convert D to meters in the formula
    return Fc, F

# Set constants for S, n, D, and us
S = 10000 # Spindle speed in rev/min
n = 2     # Number of teeth
D = 0.25    # Diameter in mm
us = 3.2  # Specific cutting energy in Ws/mm^3

# Define different depths of cut for multiple lines
depths_of_cut = [0.035, 0.07, 0.105]  # in mm

# Generate a range of CL values for plotting
CL_values = np.linspace(0.05, 0.3, 50)  # CL values in mm/tooth

# Set up the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot cutting force for each depth of cut
for d in depths_of_cut:
    cutting_forces = [calculate_cutting_force(S, n, D, CL, d, us)[0] for CL in CL_values]
    ax1.plot(CL_values, cutting_forces, label=f"Cutting Force (d = {d} mm)")

# Customize the first y-axis (Cutting Force)
ax1.set_xlabel("Chip Load (CL) [mm/tooth]")
ax1.set_ylabel("Cutting Force (Fc) [N]")
ax1.set_title("Chip Load (CL) vs Cutting Force (Fc) and Feed Rate (F)")
ax1.grid(True)
ax1.legend(loc="upper left")

# Plot Feed Rate (F) on the second y-axis
ax2 = ax1.twinx()
feed_rates = [calculate_cutting_force(S, n, D, CL, depths_of_cut[0], us)[1] for CL in CL_values]  # Use the first depth of cut for F
ax2.plot(CL_values, feed_rates, color='grey', linestyle="--", label="Feed Rate (F)")
ax2.set_ylabel("Feed Rate (F) [mm/min]")
ax2.legend(loc="upper right")

plt.show()