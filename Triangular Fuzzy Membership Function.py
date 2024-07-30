import numpy as np 
import matplotlib.pyplot as plt 
def triangular(x, a, b, c): 
    if x <= a or x >= c: 
        return 0.0 
    elif a < x <= b: 
        return (x - a) / (b - a) 
    elif b < x < c: 
        return (c - x) / (c - b) 
    elif x == b: 
        return 1.0 
    else: 
        return 0.0 
 
# Define the parameters of the triangular fuzzy set 
a = 2 
b = 5 
c = 8 
 
# Generate x values for plotting 
x_values = np.linspace(0, 10, 1000) 
 
# Calculate membership values for each x value 
membership_values = [triangular(x, a, b, c) for x in x_values] 
 
# Plotting the membership function 
plt.figure(figsize=(8, 6)) 
plt.plot(x_values, membership_values, 'b', label='Triangular Fuzzy Membership Function') 
plt.title('Triangular Fuzzy Membership Function') 
plt.xlabel('x') 
plt.ylabel('Membership') 
plt.ylim(-0.1, 1.1) 
plt.axvline(x=a, color='r', linestyle='--', label='a') 
plt.axvline(x=b, color='g', linestyle='--', label='b') 
plt.axvline(x=c, color='r', linestyle='--', label='c') 
# plt.legend() 
plt.grid(True) 
plt.show() 
