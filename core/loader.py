from spark_session import SparkSessionCreator


class DataLoader:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        session = SparkSessionCreator("local[1]", "data-loader").create_spark_session()
        return session.read.format("csv") \
            .load(self.path)
