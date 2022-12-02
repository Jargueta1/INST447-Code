'''
Name: Main.py
Author: Jorge Argueta, Blen Bizuwork, Sungwook Hwang
Class: INST 447
Descreption: extract data from csv files 
    '''

import pandas as pd 
import numpy as np
from scipy import stats

QUANTITATIV_VALUES = ["tempmax", "tempmin", "temp","feelslikemax", "feelslikemin","feelslike", "dew",  
"humidity","precip","precipprob","precipcover","snow", "moonphase", "uvindex","solarenergy","solarradiation", "visibility","cloudcover","sealevelpressure","winddir","windspeed","windgust"]
DATA_NOT_NEEDED = ["name","conditions","description","icon","stations","severerisk","preciptype","sunrise","sunset"]

## Done 
def getData(path):
    """
    description: takes file path and imports it as a df 

    input: file path
    """
    df = pd.read_csv(path) ## gets data from CSV and adds it to pd df 
    
    df = df.set_index("datetime")
    
    ## Removing non qualitatitve columns
    ## removed precitype since all of the presitaiton of the data included rain for 2021
    for s in DATA_NOT_NEEDED:
        df.pop(s)
    
    return df

## Needs to be optimize but is working 
def clean(df):
    """
    description: Takes in a data frame and removes the outliers as well as the errors that it might contain 

    input: data frame 
    Return : Normilzed Data frame 
    """
    
    ## checks for outliers and errors 
    ## needs to be optimize

    dates_with_outliers = []
    for (columnName, columnData) in df.items():
        
        mean_1 = np.mean(columnData.values)
        std_1 =np.std(columnData.values)
        outliers = []
        for y in columnData.values:
            z_score= (y - mean_1)/std_1 
            if float(np.abs(z_score)) > 3:
                outliers.append(y)
                df.drop(df.index[df[columnName] == y])

    return df
    

# Done 
def get_rainy_days(df):
  
    i = 0 
    
    df = df[df.precip >= 0.1]
    
    return df 
            
def main(): 
    
    
    
    df_2021_entry = getData("Code/raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
   
    #df_2021_normalize, df_2021_outliers = normalize(df_2021_entry) 
    
    df_clean = clean(df_2021_entry)
    
    rainy_days = get_rainy_days(df_clean)

    
    for x in QUANTITATIV_VALUES:
        print("#####################")
        print(rainy_days[x].describe())
 
    
    print(rainy_days["precip"].describe())
    
main()
