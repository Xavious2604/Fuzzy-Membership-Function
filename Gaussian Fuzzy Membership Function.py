import numpy as np 
import matplotlib.pyplot as plt 

def gaussian(x, mean, std_dev): 
 return np.exp(-0.5 * ((x - mean) / std_dev) ** 2) 
# Define the parameters of the Gaussian fuzzy set 
mean = 5  # Mean or center of the Gaussian 
std_dev = 1  # Standard deviation of the Gaussian 
# Generate x values for plotting 
x_values = np.linspace(0, 10, 1000) 
# Calculate membership values for each x value 
membership_values = gaussian(x_values, mean, std_dev) 
# Plotting the membership function 
plt.figure(figsize=(8, 6)) 
plt.plot(x_values, membership_values, 'b', label='Gaussian Fuzzy Membership Function') 
plt.title('Gaussian Fuzzy Membership Function') 
plt.xlabel('x') 
plt.ylabel('Membership') 
plt.ylim(-0.1, 1.1) 
plt.axvline(x=mean, color='r', linestyle='--', label='Gaussian Mean') 
# plt.legend() 
plt.grid(True) 
plt.show() 
