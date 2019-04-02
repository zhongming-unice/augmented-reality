import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import linalg

import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
    
goal_width=2.44
goal_height=7.32
goal_area_1=5.5
goal_area_2=18.32
penalty_area_1=16.5
penalty_area_2=40.32
corner_arc=1
flag_height=1.5
field_1=65
field_2=105

u_field=np.array([[goal_width/2,0,0],[goal_width/2,goal_height,0],     # Goal
                  [-goal_width/2,goal_height,0],[-goal_width/2,0,0],      # Goal
                  [goal_area_2/2,0,0],[goal_area_2/2,0,goal_area_1],     # Goal area
                  [-goal_area_2/2,0,goal_area_1],[-goal_area_2/2,0,0],     # Goal area
                  [penalty_area_2/2,0,0],[penalty_area_2/2,0,penalty_area_1],     # Penalty area
                  [-penalty_area_2/2,0,penalty_area_1], [-penalty_area_2/2,0,0],    # Penalty area
                  [field_1/2,0,0],[-field_1/2,0,0],     # Corners
                  [field_1/2-corner_arc,0,0],[-field_1/2+corner_arc,0,0],     # Corner radius x
                  [field_1/2,0,corner_arc],[-field_1/2,0,corner_arc],     # Corner radius y
                  [field_1/2,flag_height,0],[-field_1/2,flag_height,0]])    # Flag extremities
                  
u_w=    np.array([[goal_width/2,0,0],[goal_width/2,goal_height,0],     # Goal
                  [-goal_width/2,goal_height,0],[-goal_width/2,0,0],      # Goal
                  [goal_area_2/2,0,0],[goal_area_2/2,0,goal_area_1],     # Goal area
                  [-goal_area_2/2,0,goal_area_1],[-goal_area_2/2,0,0],     # Goal area
                  [-penalty_area_2/2,0,0],    # Penalty area
                  [-field_1/2,0,0],     # Corners
                  [-field_1/2+corner_arc,0,0],     # Corner radius x
                  [-field_1/2,0,corner_arc],     # Corner radius y
                  [-field_1/2,flag_height,0]])    # Flag extremities

N=np.shape(u_w)[0]           # Number of visible points                                    
u_w=np.vstack((np.transpose(u_w),np.ones(N)))          # Transformation to homogeneous coordinates           
         

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(u_w[0,:],-u_w[2,:],u_w[1,:])
ax.set_xlim(-35,35)
ax.set_zlim(-30,1)   
ax.set_ylim(-20,20)   
plt.show         

img=mpimg.imread('goal.jpg')
plt.imshow(img)
u_im = np.transpose(np.array(plt.ginput(N,timeout=-1)))
u_im = np.vstack((np.transpose(u_im),np.ones(N)))   
plt.close()

print(u_im)