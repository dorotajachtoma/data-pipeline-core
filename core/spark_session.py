from pyspark.sql import SparkSession

class SparkSession:

    def __init__(self, master, app_name);
        self.master = master
        self.app_name = app_name
    
    def create_spark_session():
        return SparkSession.builder().master(master)
                .appName(app_name)
                .getOrCreate()