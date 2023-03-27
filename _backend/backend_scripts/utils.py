import pandas as pd
def exc_to_dict(fname:str):
    df = pd.read_csv(fname)
    return dict(zip(df.iloc[:, 0], df.iloc[:, 1]))