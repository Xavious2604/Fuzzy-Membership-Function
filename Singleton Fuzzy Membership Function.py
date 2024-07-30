import numpy as np 
import matplotlib.pyplot as plt 
def singleton(x, mean, width): 
 if mean - width/2 <= x <= mean + width/2: 
  return 1.0 
 else: 
  return 0.0 
mean = 5  # Mean or center of the singleton 
width = 1  # Width of the singleton set 
x_values = np.linspace(0, 10, 1000) 
membership_values = [singleton(x, mean, width) for x in x_values] 
plt.figure(figsize=(8, 6)) 
plt.plot(x_values, membership_values, 'b', label='Singleton Fuzzy Membership Function') 
plt.title('Singleton Fuzzy Membership Function') 
plt.xlabel('x') 
plt.ylabel('Membership') 
plt.ylim(-0.1, 1.1) 
plt.axvline(x=mean, color='r', linestyle='--', label='Singleton Mean') 
# plt.legend() 
plt.grid(True) 
plt.show()
