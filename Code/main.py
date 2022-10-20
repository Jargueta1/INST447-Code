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
    
    ## Removing non qualitatitve columns
    data_not_needed = ["name","conditions","description","icon","stations","severerisk","preciptype"]
    
    for s in data_not_needed:
        df.pop(s)
    
    
    return df


def main(): 
    
    df_2021 = getData("raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
    df_2022 = getData("raw_data/Washington,DC,USA 2022-01-01 to 2022-09-30.csv")
    
    print("###########2021")
    print(df_2021.head())
    
    print("###########2022")
    print(df_2022.head())
    
    

    print("done")
    
main()