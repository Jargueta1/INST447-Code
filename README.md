# INST447-Code
 This repo. stores the code for our INST 447 group project

## Team proposal 
Domain for our project is weather in Washington D.C.
The data will at least include the following: 
    datetime  - datetime 
    tempmax - float 
    tempmin - float 
    temp - float 
    feelslikemac - float 
    feelslikemin - float 
    feelslike - float 
    dew - float 
    Humidity - float 
    precip - float 
    precipprob - int (0 or 100)
    precipcover - float 
    snow - float 
    snowdepth - float 
    windgust - float 
    windspeed - float 
    winddit - float 
    sealevelpressure - float 
    cloudcover - float 
    visibility - float 
    Solarradiation - float 
    solarenergy - float 
    uvindex - interger 
    moonface - float
The objective is to determine patterns in the data to create weather advisory communications 
We would focus on rainy days and what the weather seems to be around those days. 
We will use data from 2021 and the first half of 2022 to train our ML model to attempt and make a prediction graph


## Data Entry
Data has been obtained using https://www.visualcrossing.com/resources/
DF will have the following attributes with corresponding data sctructures 
The first df will be for the year of 2021, the second df will be for the first half of 2022.

## functions (not ML)
    train_model()
        Will be use to train out ML model 
    preditct()
        Will be used to attempt and predict weather
    get_Rainy_days()
        Gets the date for the days that it rained 
    rain_streaks()
        Get the streaks of how many days it rained back to back 
    get_normality()
        Gets normal values for all of attributes 
    get_outliers()
        Gets outlier i.e. values that don't fall in within normality 
    


    
