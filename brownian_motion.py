# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:58:54 2024

@author: Josh
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#Brownian motion visualisation

n = 1000 
nPaths = 100  

T = 2   
t = np.linspace(0., T, n)
dt = t[1] - t[0] 

samples = np.ones((nPaths, n))

for i in range(nPaths):
    dWt = np.sqrt(dt) * np.random.normal(size=n-1) 
    dWtCumulative = np.concatenate((np.array([0]), np.cumsum(dWt)))
    samples[i] = dWtCumulative

####################################################################

#plot 1
fig, ax = plt.subplots()
ax.set(xlim=[-0.05, 2.], ylim=[-5, 5])
plt.title('100 Realisations of Brownian Motion')
plt.plot(t, samples.T)

#####################################################################

#plot 2
fig, ax = plt.subplots()
ax.set(xlim=[-0.05, 2.], ylim=[-5, 5])
plt.title('A Realisation of Brownian Motion')

line1, = ax.plot([], [])
current_point, = ax.plot([], [], 'bo', lw=0.5)

def update(frame):
    line1.set_data(t[:frame], samples[0][:frame])
    current_point.set_data((t[frame-1],) , (samples[0][frame-1],) )

ani = animation.FuncAnimation(fig, func=update, frames=len(t), interval=10, blit=False)
plt.show()

#####################################################################


#plot 3
fig, ax = plt.subplots()
ax.set(xlim=[-0.05, 2.], ylim=[-5, 5])
plt.title('Animated Realisations in turn')

lines = []
for i in range(nPaths):     #create line holders
    line, = ax.plot([], [], c='b')   
    lines.append(line)
    
    
def init():
    for line in lines:
        line.set_data([],[])
    return lines
    
def update(frame):
    total_frames_per_line = len(t)
    current_line = frame // total_frames_per_line

    if current_line < nPaths:

        current_frame_in_line = frame % total_frames_per_line

        lines[current_line].set_data(t[:current_frame_in_line], samples[current_line][:current_frame_in_line])

    return lines


total_frames = nPaths * len(t)

ani = animation.FuncAnimation(fig, func=update, frames=total_frames, interval=10, blit=False)
plt.show()

######################################################################

# f = r"c://Users/Josh/Desktop/brownian4.gif" 
# writergif = animation.PillowWriter(fps=30) 
# ani.save(f, writer=writergif)
