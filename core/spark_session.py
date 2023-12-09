from pyspark.sql import SparkSession


class SparkSessionCreator:

    def __init__(self, master, app_name):
        self.master = master
        self.app_name = app_name

    def create_spark_session(self):
        return SparkSession.builder.master(self.master) \
            .appName(self.app_name) \
            .getOrCreate()

