from pyspark.sql.types import *
import statistics
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import *


brokers = "kafka1:9092,kafka2:9092"

spark = SparkSession \
    .builder \
    .appName("StructuredStreamingKafka") \
    .getOrCreate()

KAFKA_TOPIC = "Stream_Test"


#   spark = SparkSession \
#         .builder \
#         .appName("PySpark Structured Streaming with Kafka Demo") \
#         .master("local[*]") \
#         .config("spark.jars", "/home/cldr/streams-dev/libs/spark-sql-kafka-0-10_2.11-2.4.4.jar,/home/cldr/streams-dev/libs/kafka-clients-2.0.0.jar") \
#         .config("spark.executor.extraClassPath", "/home/cldr/streams-dev/libs/spark-sql-kafka-0-10_2.11-2.4.4.jar:/home/cldr/streams-dev/libs/kafka-clients-2.0.0.jar") \
#         .config("spark.executor.extraLibrary", "/home/cldr/streams-dev/libs/spark-sql-kafka-0-10_2.11-2.4.4.jar:/home/cldr/streams-dev/libs/kafka-clients-2.0.0.jar") \
#         .config("spark.driver.extraClassPath", "/home/cldr/streams-dev/libs/spark-sql-kafka-0-10_2.11-2.4.4.jar:/home/cldr/streams-dev/libs/kafka-clients-2.0.0.jar") \
#         .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType() \
        .add("count", IntegerType()) \
        .add("time", StringType()) \


 # Construct a streaming DataFrame that reads from testtopic
trans_det_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", brokers) \
        .option("subscribe", KAFKA_TOPIC) \
        .option("startingOffsets", "earliest") \
        .load() \
        .select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

print("Status " + str(trans_det_df.isStreaming))

#(from_json(col("value").cast("string"),schema))

    #Q1 =  trans_det_df.select(from_json(col("value"), schema).alias("parsed_value"), "timestamp")
    #Q2 =  trans_det_d.select("parsed_value*", "timestamp")


query = trans_det_df.writeStream \
            .format("console") \
            .option("truncate","false") \
            .start() \
            .awaitTermination()

# query = trans_det_df \
#     .writeStream \
#     .format("memory") \
#     .queryName("testData2") \
#     .outputMode("append") \
#     .start()