import os

import pandas as pd


def readfiles():
    return [pd.read_csv(os.path.join('data', filename), sep=',') for filename in
            os.listdir('data')]  # f(x) = i*x E (S) , where filename = x, S =


csvlist = readfiles()
# if __name__ == '__main__':
#    x = readfiles()
#    print(x)
