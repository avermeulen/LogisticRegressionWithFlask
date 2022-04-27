#========IMPORT LIBRARY===================

import pandas as pd
import numpy as np
import pickle
#============= LOAD the DATASET===========

data0 = pd.read_excel (r'./BMI_data.xlsx')
XX1 = pd.DataFrame(data0, columns= ['Weight'])
XX2 = pd.DataFrame(data0, columns= ['Height'])
YY = pd.DataFrame(data0, columns= ['Obese'])

arr_x1 = np.array([XX1])
arr_x2 = np.array([XX2])
arr_y = np.array([YY])

# print (XX1)
# print(arr_x1)
X1 = arr_x1.flatten()
print (X1)

print("--------")

X2 = arr_x2.flatten()
Y = arr_y.flatten()

X1 = X1/10
print(X1)

X2 = X2/10

# ===================INITIALIZATION=====
b0 = 0.0
b1 = 0.0
b2 = 0.0
alpha = 0.3
epochs = 1000
  


# =======TRAINING the MODEL==================
# for i in range(epochs):
#     print('Epoch ' + str(i+1), '/', epochs)
#     for j in range(len(X1)):
#         output = b0 + b1*X1[j] + b2*X2[j]
#         prediction = 1/(1 + np.exp(-(output)))
#         b0 = b0 + alpha * (Y[j] - prediction) * prediction * (1-prediction) * 1
#         b1 = b1 + alpha * (Y[j] - prediction) * prediction * (1-prediction) * X1[j]
#         b2 = b2 + alpha * (Y[j] - prediction) * prediction * (1-prediction) * X2[j]
#         print(str(j+1), 'b0:', b0, 'b1:', b1, 'b2:', b2, 'prediction:', prediction)
#         pass
#     pass
# model = [b0,b1,b2]
# # =============Save MODEL===============
# filename = 'finalized_model.sav'
# pickle.dump(model, open(filename, 'wb'))

