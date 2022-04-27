import numpy as np
import pickle

#============= LOAD the Model===========
filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

def obesity_score(weight, height):

    b0 = loaded_model[0]
    b1 = loaded_model[1]
    b2 = loaded_model[2]

    output = b0 + b1*(weight/10) + b2*(height/10)
    obesity = 1/(1 + np.exp(-(output)))
    return np.round_(obesity)