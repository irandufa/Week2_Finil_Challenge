
import pandas as pd
import numpy as np
import os
import sys

def data_format(data):
    print("Data Fromating Started...")
    data=data.rename(columns={"old_column_name":"new_column_name"
                              , "size_in_mb":"size_in_megabytes"})
    
    if 'data_column' in data.column:
        data['data_column']=pd.to_datetime(data['data_column'], errors="coerce")

        print("Data Formating Compeleted ...")
    return data
    
