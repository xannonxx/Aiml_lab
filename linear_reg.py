import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def kernel(point,xmat, k): 
    m,n = np.shape(xmat) # m = 244(rows), n = 2(cols)
    # here xmat and X are same
    weights = np.mat(np.eye((m))) # eye - identity matrix  an identity matrix 244 * 244 is created
    
    for j in range(m):
        diff = point - X[j]
        weights[j,j] = np.exp(diff*diff.T/(-2.0*k**2)) 
    
    return weights

def localWeight(point,xmat,ymat,k): 
    wei = kernel(point,xmat,k)
    W = (X.T*(wei*X)).I*(X.T*(wei*ymat.T)) 
    return W

def localWeightRegression(xmat,ymat,k): 
    m,n = np.shape(xmat) # getting dimension of matix
    
    ypred = np.zeros(m) # ypred initialized with zeros where m = 244
    
    for i in range(m):
        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k) 
    return ypred


def graphPlot(X,ypred):
    sortindex = X[:,1].argsort(0) #argsort - index of the smallest
    xsort = X[sortindex][:,0]
    plt.Figure(figsize=(14,7))
    plt.scatter(bill,tip, color='green')
    plt.plot(xsort[:,1],ypred[sortindex], color = 'red',linewidth=5)
    plt.show();


data = pd.read_csv('tips.csv')

bill = np.array(data['total_bill']) # We use only Bill amount and Tips data tip = np.array(data.tip)
tip = np.array(data['tip'])


mbill = np.mat(bill) # .mat will convert nd array is converted in 2D array mtip =  np.mat(tip)
mtip = np.mat(tip)


m= np.shape(mbill)[1]
one = np.mat(np.ones(m))

X = np.hstack((one.T,mbill.T)) # 244 rows, 2 cols one.T means transpose of matrix 'one'

ypred = localWeightRegression(X,mtip,1.5)

graphPlot(X,ypred)


