import numpy as np
from matplotlib import pyplot as plt

# Write 3D cube coordinates
X= np.array([[0,1,1,0,0,1,1,0],[0,0,1,1,0,0,1,1],[0,0,0,0,1,1,1,1]])
print(X)

# Scaling matrix
def scaling_matrix(s):
    # Scales are given in numpy array s
    # s=np.array([s_x,s_y,s_z])
    
    # Write the scaling matrix here
    S = np.identity(4)
    S[:3, :3] = np.diag(s)
    
    return S

# Translation matrix
def translation_matrix(t):
    # Translation vector is given in numpy array t
    # t=np.array([t_x,t_y,t_z])
    
    # Write the translation matrix here
    T = np.identity(4)
    T[:3, 3] = t
    
    return T

# Rotation matrix
def rotation_matrix(theta, v):
    # Axis for rotation (unit norm vector) is given 
    # is given in numpy array v
    # v=np.array([v_x,v_y,v_z])
    # Rotation angle is given in theta
    
    # Write the rotation matrix here
    st = np.sin(theta)
    ct = np.cos(theta)
    o_ct = 1-ct
    vx2= v[0]**2
    vy2= v[1]**2
    vz2= v[2]**2
    vxy = v[0]*v[1]
    vxz = v[0]*v[2]
    vyz= v[1]*v[2]
    # Rotation
    R = [[ct+vx2*o_ct, vxy*o_ct-v[2]*st, vxz*o_ct+v[1]*st],
         [vxy*o_ct+v[2]*st, ct+vy2*o_ct, vyz*o_ct-v[0]*st],
         [vxz*o_ct-v[1]*st, vyz*o_ct+v[0]*st, ct+vz2*o_ct]]
    R_v = np.identity(4)
    R_v[:3, :3] = R
    
    return R_v

# Projection function 
def im_proj(X,K_cw,f,s,o,pix):
    
    # Number of points
    n_points = np.shape(X)
    
    # Add fourth coordinate to have homogeneous coordinates
    X_h = np.vstack((X,np.ones(1,n_points[1],dtype=np.float)))
    # Write K_wc matrix
    K_wc = np.linalg.inv(K_cw)
    
    # Write K_f times Pi_0 matrix
    K_f = np.identity(3)
    K_f[0,0] = f
    K_f[1,1] = f
    K_f_Pi_0 = np.hstack((K_f,np.zeros((3,1),dtype=float)))
    
    # Write K_s matrix
    K_s = np.identity(3,dtype=float)
    K_s[:2,2] = o
    K_s[0,0] = s[0]
    K_s[1,1] = s[1]
    K_s[0,1] = s[2]
    
    
    # Write the camera matrix
    M = np.dot(K_s,np.dot(K_f_Pi_0,K_wc))
    
    # Projection in homogeneous coordinates
    #*************#
    
    # Deleting points outside image buffer
    out_buffer_1 = (X_im < 0)    
    # Floor outputs to integers
    #*************#
    
    # Output image buffer
    #*************#
    
    return im_buffer, X_im



R_cw = #*************#
t_cw = #*************#
K_cw = #*************#



f = #*************#
s = #*************#
pix = #*************#
o = #*************#


im_buffer, X_im = im_proj(X,K_cw,f,s,o,pix)
# print(X_im)
plt.imshow(im_buffer,cmap='Greys');