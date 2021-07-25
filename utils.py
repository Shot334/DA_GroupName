import pandas as pd               #DataFrame read and operations
import numpy as np                #numerical and metrix operations on data
import seaborn as sns             
import matplotlib.pyplot as plt   
import datetime as dt             #For Date Time operations
from scipy import stats           #Statistical analysis/operations
from scipy.stats import norm      #Statistical analysis/operations
import random
import matplotlib.colors as mcolors


def clean_columns(df):

  df.columns = [a.strip() for a in df.columns]          
  #Strip() is used to make space between a column name for e.g. [HongKong] = [Hong Kong]
  
  df.columns = [a.replace(',', '') for a in df.columns] 
  #replace() is used to replace a specific value with another value for e.g [Korea, Republiv of] = [Korea, Republiv of]

  Countries_list = [ col_i for col_i in df.columns if col_i not in ["Year", "Month"]] 
  #Except Year and Month all Country names are stored in a variable to convert the data type of that specific column to float

  df[Countries_list] = df[Countries_list].astype(float)
  return df

def fill_missing_values(df):
  df = df.fillna(0)
  return df.reset_index(drop=True)

def process_df(df):
    df = df.drop(['Year','Month'], axis=1)                             #dropping non-aggregated columns
    trans_df = df.T                                                     #Transposing DataFrame
    op_df = pd.DataFrame(trans_df.sum(axis=1), columns=['Visitors']) #Calculating the total sum of every country
    op_df['Countries'] = op_df.index                                    
    op_df = op_df.reset_index(drop=True)
    op_df = op_df.sort_values(by=['Visitors'], ascending=False)                         
    return op_df

def filter_by_region(df, region):
  region_list = []
  region_list = region_dict[region]
  region_list.extend(['Year','Month'])
  df = df[region_list]
  return df.reset_index(drop=True)


def filter_by_date(df, start_year, end_year):
  if (start_year > end_year):
    return Exception("Start Year Should be less than End Year")

  df = df[(df["Year"] >=  start_year) & (df["Year"] <= end_year)] 
  return df.reset_index(drop = True)

def apply_filters(df, region, start_year, end_year):
  df = filter_by_region(df, region)
  df = filter_by_date(df,start_year, end_year)
  #print("The following dataframe for {region} from {start_year} to {end_year} are as follows:" .format(region=region, start_year=start_year, end_year=end_year))
  #print(df)
  #print("Top 3 countries are:")
  #print(df.sort_values(by=['Visitors'], ascending=False).head(3))
  return df.reset_index(drop=True)

def generate_pie_chart(df):
  df['index'] = df.index
  y = df['Visitors']
  mylabels = df['Countries']
  #colors = ['yellowgreen', 'gold', 'lightskyblue', 'red', 'blue', 'green','orange', 'skyblue']
  colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = 11)
  my_explode= [0.2] * df['Countries'].count()
  plt.clf()
  fig = plt.figure(figsize=(5, 8))
  plt.pie(y, labels = mylabels, explode=my_explode, colors=colors, shadow=True, startangle=90, autopct='%1.2f%%', pctdistance=0.9, labeldistance=1.4)
  plt.legend(title = "Countrywise Analysis",loc="lower right", bbox_to_anchor=(1.3, 0.6, 1, 1))
  plt.savefig("output/pie-chart.png", bbox_inches = 'tight')


def run_data_analysis(df, region, start_year, end_year):
  global region_dict
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

  df = clean_columns(df)
  df = fill_missing_values(df)
  df = apply_filters(df, region, start_year, end_year)
  print(df)
  df = process_df(df)
  print(df.head(3))
  generate_pie_chart(df)




