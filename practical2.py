response_time = [
    120,125,118,130,122,127,124,121,129,126,123,128,125,122,131,700,127,119,650,124
]
from sklearn.ensemble import IsolationForest
import numpy as np
errors=np.array(response_time).reshape(-1,1) # reshape converts into 2D array
model = IsolationForest(contamination = 0.1,random_state = 42) # contamination gives how much from the data is anamoly ( here 2 out of 20 (10% = 0.1))
prediction  = model.fit_predict(errors) # gives -1 if anamoly else normal 
for i in prediction :
    if i== -1: 
        print("Anamoly")
    else:
        print("Normal ")



