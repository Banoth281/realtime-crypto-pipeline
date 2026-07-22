from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

spark = SparkSession.builder     .appName("CryptoRealTimeStream")     .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0")     .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("symbol", StringType(), True),
    StructField("price_usd", DoubleType(), True),
    StructField("timestamp", LongType(), True)
])

kafka_df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "crypto_topic")     .option("startingOffsets", "latest")     .load()

parsed_df = kafka_df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

query = parsed_df.writeStream     .outputMode("append")     .format("console")     .start()

query.awaitTermination()
