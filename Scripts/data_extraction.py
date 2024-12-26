import pandas as pd

def read_csv(file_path):
    print("Loading a dataset ...")

    try:
        data=pd.read_csv(file_path)
        print("Data is Loaded Successfully")
        return data
    except Exception as e:
        print(f"Data loading errer: {e}")
        return None
    