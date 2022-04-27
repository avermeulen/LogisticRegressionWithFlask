#========IMPORT LIBRARY===================

import pandas as pd
import numpy as np

from obesity import obesity_score

#============= LOAD the DATASET===========

data00 = pd.read_excel (r'./BMI_TestData.xlsx')

XXX1 = pd.DataFrame(data00, columns= ['Weight'])
XXX2 = pd.DataFrame(data00, columns= ['Height'])
YYY = pd.DataFrame(data00, columns= ['Obese'])

arr_x11 = np.array([XXX1])
arr_x22 = np.array([XXX2])
arr_yy = np.array([YYY])

X11 = arr_x11.flatten()
X22 = arr_x22.flatten()
Y0 = arr_yy.flatten()

# divide weight and height by 10
X01 = X11/10
X02 = X22/10

#============= LOAD the Model===========
# filename = 'finalized_model.sav'

# loaded_model = pickle.load(open(filename, 'rb'))

# def obesity_score(weight, height):

#     b0 = loaded_model[0]
#     b1 = loaded_model[1]
#     b2 = loaded_model[2]

#     output = b0 + b1*(weight/10) + b2*(height/10)
#     obesity = 1/(1 + np.exp(-(output)))
#     return np.round_(obesity)

#============= TEST the Model on Training dataset===========
scorecard = []

for i in range(len(X01)):
    # output = b0 + b1*X01[i] + b2*X02[i]
    # output_values = 1/(1 + np.exp(-(output)))
    # print(X01[i], X02[i])
    
    output_values = obesity_score(X01[i]*10, X02[i]*10)
    
    print(str(i+1), 'output_value:', output_values)
    
    if (output_values > 0.5):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass
    pass


# Calculate the fraction of correct answers

print('\n','accuracy:', ((sum(scorecard==Y0))/(len(X01))*100), '%')

