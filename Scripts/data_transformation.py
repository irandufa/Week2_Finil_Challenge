import numpy as np
import os
import sys
import numpy as np
import os
import sys

def data_transform(data):
    print("Transforming Data ...")

    if 'size_in_mb' in data.columns:
        data['size_in_mb']=data['size_in_bytes']/(1024*1024)
    if 'value_column' in data.columns:
        data['log_value']=np.loglp(data['value_column'])

        print("Data Transformation Finished ..")
    return data

