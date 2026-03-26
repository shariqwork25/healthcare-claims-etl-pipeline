from pyspark.sql import SparkSession
from utils.edi_parser import parse_edi_837

spark = SparkSession.builder     .appName("EDI Claims Pipeline")     .getOrCreate()

claims = parse_edi_837("data/sample_837.txt")

df = spark.createDataFrame(claims)

# Bronze Layer
df.write.mode("overwrite").json("data/bronze_claims")

# Silver Layer
clean_df = df.dropna()
clean_df.write.mode("overwrite").json("data/silver_claims")

# Gold Layer
gold_df = clean_df.groupBy("provider_id").sum("amount")
gold_df.write.mode("overwrite").json("data/gold_claims")