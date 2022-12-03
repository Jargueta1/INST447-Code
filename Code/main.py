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
"humidity","precip","precipcover","snow", "moonphase", "uvindex","solarenergy","solarradiation", "visibility","cloudcover","windspeed","windgust"]

DATA_NOT_NEEDED = ["name","conditions","description","icon","stations","severerisk","preciptype","sunrise","sunset","sealevelpressure","precipprob","winddir"]

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
    
    # iterizes by the column name through all of the values and removes values that are more than 3 zcores away from the mean. This includes NaN and empty cells

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
    
    
    return  df.groupby(pd.Grouper(key='datetime',freq='M')).mean()

def by_month_sum(df):
      
    return  df.groupby(pd.Grouper(key='datetime',freq='M')).sum()

def temp_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen temperature and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and regression value as value 
    
    '''
    return 

def feelslike_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen feelslike and rain precipitation 
    
    input: df
    
    return: dictionary with feelslike as key and regression value as value 
    
    '''
    return 

def dew_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen dew and rain precipitation 
    
    input: df
    
    return: dictionary with dew as key and regression value as value 
    
    '''
    return 

def humidity_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen huminity and rain precipitation 
    
    input: df
    
    return: dictionary with huminity as key and regression value as value 
    
    '''
    return 

def precipcover_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen precipiration cover and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and precipitation cover value as value 
    
    '''
    return 

def snow_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen snow and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and snow value as value 
    
    '''
    return 

def moonphase_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen moonphase and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and moonphase value as value 
    
    '''
    return 
def uvindex_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen uvindex and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and uvinex value as value 
    
    '''
    return 
def solarenergy_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen solar energy and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and solar energy value as value 
    
    '''
    return 
def solarradiation_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen solar radiation and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and solar radiation value as value 
    
    '''
    return 
def visibility_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen visibility and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and visibility value as value 
    
    '''
    return 
def cloudcover_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen cloud cover and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and cloud cover value as value 
    
    '''
    return 

def windspeed_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen wind speed  and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and wind speed  value as value 
    
    '''
    return 

def windgust_rain(df):
    '''
    description: Takes in DF, plots and determines the relation ship betwen wind gust  and rain precipitation 
    
    input: df
    
    return: dictionary with temperature as key and wind gust  value as value 
    
    '''
    return 

def analysis(df):
    '''
    description: runs all of the analysis functions and prints out tier list of varaibles by highest regretion values
    
    input: df
    
    return: none 
    
    '''
    
    df_by_month_average = by_month_average(df)
    
    df_by_month_average.plot(title="Average by Month")
    
    plt.show()
    
    df_by_month_sum = by_month_sum(df)
    
    df_by_month_sum.plot()
    plt.show()
    
    
def main(): 
    
    df = getData("Code/raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
    
    df = clean(df) ## cleans out outliers and errors 
    
    df = get_rainy_days(df) ## gets only columns containing rainy days
 
    df.reset_index(inplace=True)   
    df.index = pd.to_datetime(df['datetime'],format='%m/%d/%y %I:%M%p') ## This is done so that we are able to use group by
 
    
    
    analysis(df)
    
    
    
main()
