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
This data source was chosen because of the already formatted data and the comprehensiveness 
DF will have the following attributes with corresponding data sctructures 
The first df will be for the year of 2021, the second df will be for the first half of 2022.

## functions -- Not finalize 
    
    rainy_days()
        Gets the date for the days that it rained 
        will return a list containing datetime objects for rainy days 
    rain_streaks()
        Get the streaks of how many days it rained back to back 
        will return a dictionary with keys for the number of rows that it rained and values will be the days
    normalize()
        Gets normal values for all of attributes and takes out outliers
        will return a duple of normal values and outliers 
    rain_by_month()
        Will return a summary of rain by months
            graph of how much it rained each month
            tier list of how much it rained per month 
            average rain per month 
    snow_by_month()
        Will return a summary of rain by months
            graph of how much it rained each month
            tier list of how much it rained per month 
            average rain per month 
    wind_by_month()
        Will return a summary of rain by months
            graph of how much it rained each month
            tier list of how much it rained per month 
            average rain per month 
    
## ML functions() -- Not finalize 
    train()
        will Train the ML model 
    predict_rain()
        wil take in values and predict weather or not it will rain 


## Intructions and requirements for running 
Pyhon version 3.9 is used 
The main library wil be Pandas 
The code will also be run in a virtual anadcoda environment

    
## Current Status 
need to optimize normalize function