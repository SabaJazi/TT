import numpy as np
from pykalman import KalmanFilter
from matplotlib import pyplot as plt

Measured=np.load("ballTrajectory.npy")
while True:
   if Measured[0,0]==-1.:
       Measured=np.delete(Measured,0,0)
   else:
       break
numMeas=Measured.shape[0]

MarkedMeasure=np.ma.masked_less(Measured,0)

Transition_Matrix=[[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]]
Observation_Matrix=[[1,0,0,0],[0,1,0,0]]

xinit=MarkedMeasure[0,0]
yinit=MarkedMeasure[0,1]
vxinit=MarkedMeasure[1,0]-MarkedMeasure[0,0]
vyinit=MarkedMeasure[1,1]-MarkedMeasure[0,1]
initstate=[xinit,yinit,vxinit,vyinit]
initcovariance=1.0e-3*np.eye(4)
transistionCov=1.0e-4*np.eye(4)
observationCov=1.0e-1*np.eye(2)
kf=KalmanFilter(transition_matrices=Transition_Matrix,
            observation_matrices =Observation_Matrix,
            initial_state_mean=initstate,
            initial_state_covariance=initcovariance,
            transition_covariance=transistionCov,
            observation_covariance=observationCov)

(filtered_state_means, filtered_state_covariances) = kf.filter(MarkedMeasure)
plt.plot(MarkedMeasure[:,0],MarkedMeasure[:,1],'xr',label='measured')
plt.axis([0,520,360,0])
#plt.hold(True)
plt.plot(filtered_state_means[:,0],filtered_state_means[:,1],'ob',label='kalman output')

#state_std1 = np.sqrt(filtered_state_covariances[:,0] )
#state_std2 = np.sqrt(filtered_state_covariances[:,2])

#state_std=np.sqrt(filtered_state_covariances)

# = [np.std(MarkedMeasure[:i]) for i in range(len(MarkedMeasure))]
#plt.plot(measurement_std,MarkedMeasure[:,1], 'Dg', label='measurment std')

#plt.plot(state_std[:,0],state_std2[:,2],'Dc',label='kalman output std')

#plt.plot(MarkedMeasure[:,1],state_std[:,0], 'Dc', label='kalmanx -filter output std')
#plt.plot(MarkedMeasure[:,1],state_std2[:,2], '-r', label='kalman y-filter output std')


#plt.plot(np.std(filtered_state_covariances[:,0]),np.std(filtered_state_covariances[:,1] ),'Dg',label='kalman uncertainty')
plt.legend(loc=2)
plt.title("Constant Velocity Kalman Filter")
plt.show()

#print("Standard Deviation of sample is % s " % (np.std(filtered_state_covariances)))


#------------------------------------------------------------------------------
#print(filtered_state_covariances)
#print("-----------------------------")
#print (state_std)




#---------------------------------------
# 2x2 array
#print(MarkedMeasure)

#print(state_std)
# we want the first 2 of the diagnol shape
#flattening the diagnal array

#state_std.diagonal(0,0)
flattende_covariance=state_std[:,:,0]
#print(flattende_covariance)
my2d_covariance_x=flattende_covariance[:,0]
my2d_covariance_y=flattende_covariance[:,2]
#my2d_covariance=np.vstack((my2d_covariance_x, my2d_covariance_y)).T
my2d_covariance=np.add(my2d_covariance_x,my2d_covariance_y)
print(my2d_covariance)

'''
def flatten_diagonally(x, diags=None):
    diags = np.array(diags)
    if x.shape[1] > x.shape[0]:
        diags += x.shape[1]-x.shape[0]
    n = max(x.shape)
    ndiags = 2*n-1
    i,j,k = np.indices(x.shape)
    d = np.array([])
    for ndi in range(ndiags):
        if diags != None:
            if not ndi in diags:
                continue
        d = np.concatenate((d,x[i==j+(n-1)-ndi]))
    return d

flatten_diagonally(state_std)

#------------buble plot-----------

#X=MarkedMeasure[:,0]
#Y=MarkedMeasure[:,1]
s=my2d_covariance
plt.scatter('X', 'Y',
         s,
         alpha=0.5,
         data=MarkedMeasure[:,0:1])
plt.xlabel("X", size=16)
plt.ylabel("Y", size=16)
plt.title("Bubble Plot with Matplotlib", size=18)

'''