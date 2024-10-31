#%% load packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#%%

# scrape data for all seasons


#%% 

# setup list of urls
urls = ['https://www.basketball-reference.com/leagues/NBA_2024_per_game.html', 
       'https://www.basketball-reference.com/leagues/NBA_2023_per_game.html', 
       'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html', 
       'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html', 
       'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2018_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2017_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2016_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2015_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2014_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2013_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2012_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2011_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2010_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2009_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2008_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2007_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2006_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2005_per_game.html',
       'https://www.basketball-reference.com/leagues/NBA_2004_per_game.html',]


# create empty list to store dataframes
df_list = []

# create a counter variable for the loop
i = 0

# loop creates a dataframe for each year
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # scrape table
    table = soup.find_all('table')[0]

    # scrape titles of table
    title_row = table.find_all('tr')[0]
    titles = title_row.find_all('th')[1:]
    titles = [title.text.strip() for title in titles]
    titles

    # create dataframe with titles
    df_list.append(pd.DataFrame(columns = titles))
    

    # add data to df
    data_list = [] # create empty list

    all_data_rows = table.find_all('tr')[1:] # scrape rows of data

    for row in all_data_rows: # scrape individual data points and append to list
        single_row = row.find_all('td')
        data_points = [data.text.strip() for data in single_row]
        data_list.append(data_points)

    for row in data_list: # remove empty rows
        if row == []:
            data_list.remove(row)
        
    for row in data_list: # add data to df
        length = len(df_list[i])
        df_list[i].loc[length] = row
        
    i = i + 1

# print df_list    
df_list



#%% add 'year' column to each dataframe
year = 2024

for df in df_list:
    df.insert(29, 'Year', np.repeat(year, len(df)))
    year = year - 1

#%% separate 'df_list' into individual dataframes
df_2024 = df_list[0]
df_2023 = df_list[1]
df_2022 = df_list[2]
df_2021 = df_list[3]
df_2020 = df_list[4]
df_2019 = df_list[5]
df_2018 = df_list[6]
df_2017 = df_list[7]
df_2016 = df_list[8]
df_2015 = df_list[9]
df_2014 = df_list[10]
df_2013 = df_list[11]
df_2012 = df_list[12]
df_2011 = df_list[13]
df_2010 = df_list[14]
df_2009 = df_list[15]
df_2008 = df_list[16]
df_2007 = df_list[17]
df_2006 = df_list[18]
df_2005 = df_list[19]
df_2004 = df_list[20]   

#%% concat all dataframes in one
final_df = pd.concat([df_2024, df_2023, df_2022, df_2021, df_2020, df_2019, df_2018, df_2017, df_2016, df_2015, df_2014, df_2013, df_2012, df_2011, df_2010, df_2009, df_2008, df_2007, df_2006, df_2005, df_2004])
final_df    

#%%
final_df.to_csv(r'C:/Users/Zachary Chan/Downloads/Basketball Project/basketball.csv')

