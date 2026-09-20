#reading the file
with open ("application.log",'r') as file :
    logs = file.readlines()
print(logs)
for i in logs:
    print(i.split())

# now we are going to parse  -  fetching the useful info 
logger = "2026-08-18 10:01:01 INFO UserService Request successful"
parse = logger.split()
print(parse[0]) # to acess only date 

print("Date: ",parse[0])
print("Time: ",parse[1])
print("level: ",parse[2])
print("service request : ",parse[3])
print("Type: ",parse[-1])
count =0
for i in logs:
    if "ERROR" in i:
        count +=1
print("Errors = " ,count)

#using the counter function to calculate the number of errors  in a particular time frame 
from collections import Counter 
error_by_minute = Counter()
info_by_minute = Counter()
for i in logs:
    parts = i.split()
    if "ERROR" in i:
        minute = parts[1][0:5]
        error_by_minute[minute] +=1
    if "INFO" in i:
        minute = parts[1][:5]
        info_by_minute[minute] +=1
print(info_by_minute)
print(error_by_minute)
dict = info_by_minute |error_by_minute
print(dict)

# performing the single rule bsed detection 
threshold = 3 # defining a threshold 
for min,count in error_by_minute.items():
    if count>3:
        print("ANOMOLY: ",min,"had ",count,"errors")

# using isoltionforest for namoly detection 
from sklearn.ensemble import IsolationForest
import numpy as np
errors = np.array([[2],[5],[100],[4],[10],[200]])
model = IsolationForest(contamination=0.1, random_state= 42)
model.fit(errors) # model starts analysing errors
predict = model.predict (errors)
print(predict)
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.plot(errors, 'bo-', label="Errors")  # blue dots with lines
plt.ylabel("Error Values")
plt.xlabel("Index")
plt.title("Error Data with Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()
