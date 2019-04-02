import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd



# Load from text file
tp= np.loadtxt('teapot.txt')
# Number of points in the cloud
n_points = np.shape(tp)
# Transpose and add a fourth coordinate with unitary value 
# (homogeneous coordinates)
tp = np.hstack((tp,np.ones((n_points[0],1),dtype=np.float))).T
# Save it in a data frame
df = pd.DataFrame({"x" : tp[0,:], "y" :tp[1,:], "z" : tp[2,:], 
                                                "w": tp[3,:]})

# Scaling matrix
def scaling_matrix(s):
    # Scales are given in numpy array s
    # s=np.array([s_x,s_y,s_z])
    S = np.identity(4)
    S[:3,:3] = np.diag(s)
    # Write the scaling matrix here
    #******************************
    
    return S

# Translation matrix
def translation_matrix(t):
    # Translation vector is given in numpy array t
    # t=np.array([t_x,t_y,t_z])
    T  = np.identity(4)
    T[:3,3] = t
    # Write the translation matrix here
    #******************************
    
    return T

# Rotation matrix
def rotation_matrix(theta, v):
    # Axis for rotation (unit norm vector) is given 
    # is given in numpy array v
    # v=np.array([v_x,v_y,v_z])
    # Rotation angle is given in theta
    st = np.sin(theta)
    ct = np.cos(theta)
    vx = v[0]
    vy = v[1]
    vz = v[2]
    R  = [[ct+vx**2*(1-ct),vy*vx*(1-ct)-vz*st,vx*vz*(1-ct)+vy*st],[vx*vy*(1-ct)+vz*st,ct+vy**2*(1-ct), vy*vz*(1-ct)-vx*st],[vx*vz*(1-ct)-vy*st,vy*vz*(1-ct)+vx*st,ct+vz**2*(1-ct)]]
    R_v = np.identity(4)
    R_v[:3,:3] = R
    # Write the rotation matrix here
    #******************************
    
    return R_v

# Update of the scatter plot after transformation
def update_graph(num):
    # Load point cloud from data frame
    tp=np.vstack((df['x'],df['y'],df['z'],df['w']))
    angle = num*0.01
    # Create uniform scaling matrix 
    #******************************
    s = np.array([1,1,1])
    M = scaling_matrix(s)
    # Compose M with rotation matrix
    #******************************
    t = np.array([0,0,0])
    M = np.dot(translation_matrix(t),M)
    # Compose M with translation matrix
    #******************************
    v = np.array([6,0,0])
    M = np.dot(rotation_matrix(angle, v),M)
    # Apply composed transformation to the point cloud
    #******************************
    tp_r = np.dot(M,tp)
    # Update scatter plot
    graph._offsets3d = (tp_r[0,:], tp_r[1,:], tp_r[2,:])
    return graph

# 3D figure generation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('Teapot')

# 3D scatter plot
graph = ax.scatter(tp[0,:], tp[1,:], tp[2,:])
# # Change axis limits if necessary
ax.set_xlim3d(-8, 8)
ax.set_ylim3d(-8, 8)
ax.set_zlim3d(-1, 8)

# Animation function
ani = matplotlib.animation.FuncAnimation(fig, update_graph,1000, 
                                            interval=1, blit=False)

# # Set up formatting for the movie files
 Writer = matplotlib.animation.writers['ffmpeg']
 writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
 # Save animation
 ani.save('teapot.mp4', writer=writer)

plt.show()