# import pyspark
# print(pyspark.__version__)
import os 
import sys  
# defining the session before starting the session (starting session for application)
from pyspark.sql import SparkSession
os.environ["PYSPARK_PYTHON"]= sys.executable # setting the python executable for spark 
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable #setting the python version 
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
spark = SparkSession.builder\
.appName("MyApp")\
.master("local[*]")\
.getOrCreate() 

data = [
    ("Server 1",67), #(server_name,cpu_usage)
    ("Server 2",76),
    ("Server 3",89),
    ("Server 4",92),
    ("Server 5",56),
    ("Server 6",43),
    ("Server 7",77),
] # creating data for application 

column = ["Server Name","CPU Usage"] # creating column name for application 
df = spark.createDataFrame(data,column) #creating df
df.show() # showing df in tabular form 
df.stop() # stopping the spaark session for application
