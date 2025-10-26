from pyspark.sql import SparkSession
import psycopg2

class DatabaseConnector:
    
    def __init__(self, spark_path, pg_config):
        self.spark_path = spark_path
        self.pg_config = pg_config
        self.spark = SparkSession.builder \
            .appName("ETL") \
            .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
            .getOrCreate()

    