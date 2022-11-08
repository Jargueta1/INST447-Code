'''
Name: Main.py
Author: Jorge Argueta, Blen Bizuwork, Sungwook Hwang
Class: INST 447
Descreption: extract data from csv files 
    '''

import pandas as pd 
import numpy as np
from scipy import stats


def getData(path):
    """
    description: takes file path and imports it as a df 

    input: file path
    """
    df = pd.read_csv(path) ## gets data from CSV and adds it to pd df 
    
    df = df.set_index("datetime")
    
    ## Removing non qualitatitve columns
    data_not_needed = ["name","conditions","description","icon","stations","severerisk","preciptype","sunrise","sunset"]
    
    for s in data_not_needed:
        df.pop(s)
    
    
    return df

def normalize(df):
    
    
    ## checks for outliers 
    ## needs to be optimize
    ## if any data point is an outlier, it movoes the whole column there 
    
    
    
    
    ## Might want to change this to use np. by just getting column names 
    dates_with_outliers = []
    for (columnName, columnData) in df.iteritems():
        
        mean_1 = np.mean(columnData.values)
        std_1 =np.std(columnData.values)
        print("checking for outliers in " , columnName, " ...")
        outliers = []
        for y in columnData.values:
            z_score= (y - mean_1)/std_1 
            if float(np.abs(z_score)) > 3:
                outliers.append(y)
                dates_with_outliers.append(df.index[df[columnName] == y])
        print("found ", len(outliers), " outliers")

    outlier_dict = {}
    
    i = 0
    for i in range(len(dates_with_outliers)):
        outlier_dict[dates_with_outliers[i][0]] = df.loc[dates_with_outliers[i]].to_dict('split')
    
    dates_with_outliers_normalized = []
    
    for x in dates_with_outliers:
        
        if x[0] not in dates_with_outliers_normalized:
            dates_with_outliers_normalized.append(x[0])
    
    
    for x in dates_with_outliers_normalized:
        df = df.drop(x)
    
    
    template_dict = {}    
    for x in list(outlier_dict.keys()): 
        template_dict[x] = outlier_dict[x]

    index_list = []
    column_list = []
    data_list = []

    
    for x in list(template_dict.items()):
        index_list.append(x[1]['index'][0])
        column_list.append(x[1]['columns'])
        data_list.append(x[1]['data'])
    
    column_list = column_list[0]
    
    dict_to_df = {"index": index_list}
        
    data_list_chunk = []
    
    i = 0 
    for i in range(len(column_list)):
        j = 0
        chunked_list = []
        for j in range(len(data_list)):
            chunked_list.append(data_list[j][0][i])
        dict_to_df[column_list[i]] = chunked_list

    outliers_df = pd.DataFrame.from_dict(dict_to_df)
    
    outliers_df = outliers_df.set_index("index")

    return df, outliers_df


def main(): 
    
    df_2021_entry = getData("raw_data/Washington,DC,USA 2021-01-01 to 2021-12-31.csv")
    df_2022_entry = getData("raw_data/Washington,DC,USA 2022-01-01 to 2022-09-30.csv")
    
    df_2021_normalize, df_2021_outliers = normalize(df_2021_entry) 
    df_2022_normalize, df_2022_outliers = normalize(df_2022_entry) 
    

    print("###########2021")
    print(df_2021_normalize.head())
    
    print("###########2021entry")
    print(df_2021_entry.head())
    
    print("###########2021outliers")
    print(df_2021_outliers.head())

    
    print("done")
    
main()