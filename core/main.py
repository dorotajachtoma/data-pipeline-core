from loader import DataLoader

loader = DataLoader("/Users/mac/Workspace/data-pipeline-core/data/")
'''
    Getting columns as CSV files have header with column names: option(header, true) and option(interSchema, true)
'''
loader.load_data()
columns = loader.get_columns()



