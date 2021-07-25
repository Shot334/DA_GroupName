#import argparse
import pandas as pd

#Below library uses system path, operating system path to access the data within specific System and also used to save the ouput
#For this assignment we are using repl.it system
import os, sys

#dir_path = Main path of Directory 
dir_path = os.path.dirname(os.path.realpath(__file__)) 
#parent_dir_path contains Parent direcotry of folder
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

#the path which contains Main folder of  the project
current_dir_path = os.path.join(parent_dir_path, "Monthly_Visitors")

sys.path.insert(0, current_dir_path) #inserting specific path
os.chdir("./Monthly_Visitors") #to change the directory

from Monthly_Visitors.src.utils import run_data_analysis

#This is used acces the main function which is combined of all small-functions
if __name__ == "__main__":
  

  region_dict =   {"Africa":["Africa"], 
                 "Europe":['United Kingdom', 'Germany', 'France','Italy', 'Netherlands', 'Greece', 'Belgium & Luxembourg', 'Switzerland',
                                'Austria', 'Scandinavia', 'CIS & Eastern Europe'], 
                 "South East Asia":['Brunei Darussalam', 'Indonesia', 'Malaysia','Philippines', 'Thailand', 'Viet Nam', 'Myanmar'],
                 "North America":['USA','Canada'],
                 "Middle East":['Saudi Arabia','Kuwait','UAE'],
                 "South Asia Pacific":['India', 'Pakistan','Sri Lanka'],
                 "Australia":['Australia', 'New Zealand'],
                 "Asia Pacific":['Japan', 'Hong Kong', 'China', 'Taiwan', 'Korea Republic Of']
                }

  missing_values = [' na '] 
  df = pd.read_csv("data/MonthyVisitors.csv", na_values = missing_values)

  df["Year"] = df["Year"].astype(int) #Converting data type as int
  min_year = df["Year"].min() #Min value from ['Year'] column
  max_year = df["Year"].max() #Max value from ['Year'] column

  all_available_region = ", ".join(list(region_dict.keys()))
  #It gives space between regions when it is printed

  print("The available regions are {}. Please pick one of the regions mentioned above. Year ranges from {} to {}.".format(all_available_region, min_year, max_year))
  #print() to print the information/message

  region = str(input("Enter Region : ")) #Taking input from user for region as string value
  try:
    start_year = int(input("Enter Year to Start : ")) #Taking input from user for start year as an integer value
  except:
    start_year = ""
  
  try:
    end_year = int(input("Enter Year to End : "))  #Taking input from user for start year as an integer value
  except:
    end_year = ""
  
  #Code foor default region
  if region == "":
    region = "Europe"
    print("No input Region is passed, choosing default region : {}".format(region))
  
  if start_year == "" or start_year == 0:
    start_year = 1997
    print("No input start year is passed, choosing defaul start year : {}".format(start_year))

  if end_year == "" or end_year == 0:
    end_year = 2007
    print("No input end year is passed, choosing defaul end year : {}".format(end_year))

  print("You have picked {} Region which consists of {}and and have picked {} to {} for its year range.".format(region, ", ".join(region_dict[region]), start_year, end_year))

  #calling function to display the required data
  run_data_analysis(df, region, start_year, end_year)