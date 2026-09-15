#imports
import pandas as pd

#load data
mod5_task1_json = pd.read_json('mod5_task1.json')
#preview json data 
print(mod5_task1_json.head())

#convert to csv
mod5_task1_json.to_csv('mod5_task1.csv', index=False)
#review csv data
mod5_task1_csv = pd.read_csv('mod5_task1.csv')
print(mod5_task1_csv)