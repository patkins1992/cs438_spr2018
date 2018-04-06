import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
X = np.array([  [1,0,1,1,1,1,1,1,1], #Up
                [1,1,1,1,1,0,1,1,1], #Right  
                [1,1,1,1,1,1,1,0,1], #Down 
                [1,1,1,0,1,1,1,1,1], #Left
                
                [1,0,1,0,1,0,1,1,1]  #Test Left and right
                ])
    
# output dataset [Up,right,Down,left]           
y = np.array([[1,0,0,0], #Up
              [0,1,0,0], #Right
              [0,0,1,0], #Down
              [0,0,0,1], #left
              ])

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)
c_0=0; c_1=0;c_2=0; c_3=0; 
# initialize weights randomly with mean 0
syn0 = 2*np.random.random((9,4)) - 1

for iter in range(1000):
    i =np.random.randint(0,4)
    if i==0:
        c_0+=1
    elif i==1:
        c_1+=1
    elif i==2:
        c_2+=1 
    elif i==3:
        c_3+=1
    # forward propagation
    l0 = X[i]
    l0.shape=(1,9)
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y[i] - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)
    l1_delta.shape=(1,4)
    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print("Output After Training:")


l0 = X[4]
l1= nonlin(np.dot(l0,syn0))

print(l1)
