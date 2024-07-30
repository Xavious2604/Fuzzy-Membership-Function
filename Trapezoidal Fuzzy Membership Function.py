import numpy as np 
import matplotlib.pyplot as plt 
def trapezoidal(x, a, b, c, d): 
    if x <= a or x >= d: 
        return 0.0 
    elif a < x <= b: 
        return (x - a) / (b - a) 
    elif b < x <= c: 
        return 1.0 
    elif c < x < d: 
        return (d - x) / (d - c) 
    else: 
        return 0.0 

a = 2 
b = 3 
c = 6 
d = 8 
 
x_values = np.linspace(0, 10, 1000) 
 
membership_values = [trapezoidal(x, a, b, c, d) for x in x_values] 
 
# Plotting the membership function 
plt.figure(figsize=(8, 6)) 
plt.plot(x_values, membership_values, 'b', label='Trapezoidal Fuzzy Membership Function') 
plt.title('Trapezoidal Fuzzy Membership Function') 
plt.xlabel('x') 
plt.ylabel('Membership') 
plt.ylim(-0.1, 1.1) 
plt.axvline(x=a, color='r', linestyle='--', label='a') 
plt.axvline(x=b, color='g', linestyle='--', label='b') 
plt.axvline(x=c, color='g', linestyle='--', label='c') 
plt.axvline(x=d, color='r', linestyle='--', label='d') 
# plt.legend() 
plt.grid(True) 
plt.show()
