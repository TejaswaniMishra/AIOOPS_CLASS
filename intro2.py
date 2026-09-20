from pyspark.sql import SparkSession
spark = SparkSession.builder\
.appName("MY APP")\
.master("local[*]")\
.getOrCreate()
df= spark.read.csv("server.csv",header=True, inferSchema=True)
df.show()
df.printSchema()  # printing datatype of each column 
df.select("server","error").show()
 
