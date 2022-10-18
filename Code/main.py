'''
Name: Main.py
Author: Jorge Argueta, Blen Bizuwork, Sungwook Hwang
Class: INST 447
Descreption: extract data from csv files 
    '''

import pandas as pd 


def getData(path):
    """
    description: takes file path and imports it as a df 

    input: file path
    """
    df = pd.read_csv(path) ## gets data from CSV and adds it to pd df 
    
    df = df.set_index("datetime")
    
    ## Removing columns not needed
    data_not_needed = ["name", "sunrise","sunset","conditions","description","icon","stations","severerisk"]
    
    for s in data_not_needed:
        df.pop(s)
    
    
    return df


def main(): 
    
    df = getData("raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
    
    print(df.head())

    print("done")
    
main()