import pandas as pd
import os




def readfiles():
    files = [] # Files is a list
    for i,filename in enumerate(os.listdir('data')):    # List filenames of data dir
        files.append(i) # Increase files list size (up to # of files in data dir)
        files[i] = pd.read_csv(os.path.join('data', filename), sep=',') # files is a list of DataFrames (pandas type)
    return files

csvlist = readfiles()




