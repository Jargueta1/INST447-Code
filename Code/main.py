'''
Name: Main.py
Author: Jorge Argueta, Blen Bizuwork, Sungwook Hwang
Class: INST 447
Descreption: extract data from csv files 
    '''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

QUANTITATIV_VALUES = ["tempmax", "tempmin", "temp","feelslikemax", "feelslikemin","feelslike", "dew",  
"humidity","precip","precipcover","snow", "moonphase", "uvindex","solarenergy","solarradiation", "visibility","cloudcover","winddir","windspeed","windgust"]

DATA_NOT_NEEDED = ["name","conditions","description","icon","stations","severerisk","preciptype","sunrise","sunset","sealevelpressure","precipprob"]

def getData(path):
    """
    description: takes file path and imports it as a df 

    input: file path
    """
    df = pd.read_csv(path) ## gets data from CSV and adds it to pd df 
    
    df = df.set_index("datetime") ## sets the index to be the date that the data was collected 
    df.index = pd.to_datetime(df.index) ##changes the index to datetime object
    
    ## Removing non qualitatitve columns
    ## removed precitype since all of the precipitation of the data included rain for 2021 therefore it's safe to assume that 
    ## any prescipitation is refering to rain
    for s in DATA_NOT_NEEDED:
        df.pop(s)
    
    return df

def clean(df):
    """
    description: Takes in a data frame and removes the outliers as well as the errors that it might contain 

    input: data frame 
    Return : Normilzed Data frame 
    """
    
    # iterizes by the column name through all of the values and removes values that are more than 3 zcores away from the mean. This increades NaN and empty cells
    
    dates_with_outliers = []
    for (columnName, columnData) in df.items():
        mean_1 = np.mean(columnData.values) ## gets the mean for that column 
        std_1 =np.std(columnData.values) ## gets the standard deviation for that column 
        for y in columnData.values:
            z_score= (y - mean_1)/std_1  ## Gets z-score of the value
            if float(np.abs(z_score)) > 3:
                df.drop(df.index[df[columnName] == y])
    return df


def get_rainy_days(df):
    """
    description: takes the dataframe and removes any rows where it did not rain

    input: data frame 
    Return : Normilzed Data frame 
    """
    df = df[df.precip >= 0.1] ##removes columns where the precipitation was less than 0.1 
    
    return df 

def by_month_average(df):
    
    
    df.reset_index(inplace=True)    
    df.index = pd.to_datetime(df['datetime'],format='%m/%d/%y %I:%M%p')
    
    return  df.groupby(pd.Grouper(key='datetime',freq='M')).mean()


def by_month_sum(df):
      
    return  df.groupby(pd.Grouper(key='datetime',freq='M')).sum()

        
def main(): 
    
    df = getData("Code/raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
    
    df = clean(df) ## cleans out outliers and errors 
    
    df = get_rainy_days(df) ## gets only columns containing rainy days
 
    df_by_month_average = by_month_average(df)
    
    df_by_month_average.plot()
    plt.show()
    
    df_by_month_sum = by_month_sum(df)
    
    df_by_month_sum.plot()
    plt.show()
 
    
    
main()
