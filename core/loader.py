from spark_session import SparkSessionCreator


class DataLoader:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        session = SparkSessionCreator("local[1]", "data-loader").create_spark_session()
        return session.read.format("csv") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load(self.path)

    def get_columns(self):
        df = self.load_data()
        return df.columns

