#%% load packages
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

#%% load basketaball data

basketball_df = pd.read_csv('C:/Users/Zachary Chan/Downloads/Basketball Project/basketball.csv')

#%%

# Data Cleaning


#%% view data

basketball_df.columns
basketball_df.head()
basketball_df.describe()

#%% Remove duplicate players

basketball_df = basketball_df.drop_duplicates(subset = ['Player'], keep = 'first')


#%% Simplify position column

# iterate over 'Pos' column so that it only takes the first 2 characters
index = 0
for i in basketball_df['Pos']:
    basketball_df.iloc[[index],[2]] = i[:2]
    index += 1
    
# iterate over 'Pos' column so that any dashes (-) are removed
index = 0
for i in basketball_df['Pos']:
    basketball_df.iloc[[index],[2]] = i.replace('-', '')
    index += 1
    

#%% plot avg 3PA over years
grouped_df = basketball_df.groupby('Year').mean('3PA')
grouped_df['3PA']

grouped_df.plot.line(y='3PA', title='Avg. 3PA Over Years (2004-2024)', figsize=(20,8))
plt.xticks(np.arange(2004, 2025, 1.0))

#%% plot avg 3PA grouped by position over years
grouped_df = basketball_df.groupby(['Year', 'Pos'])['3PA'].mean().unstack()
grouped_df.plot.line(title = 'Avg. 3PA Over Years(2004-2024) by Position', figsize=(20,8), legend = True)
plt.xticks(np.arange(2004, 2025, 1.0))

#%% plot avg 3P% over years
grouped_df = basketball_df.groupby('Year').mean('3P%')
grouped_df['3P%']

grouped_df.plot.line(y='3P%', title='Avg. 3P% Over Years (2004-2024)', figsize=(20,8))
plt.xticks(np.arange(2004, 2025, 1.0))

#%% plot avg 3PA grouped by position over years
grouped_df = basketball_df.groupby(['Year', 'Pos'])['3P%'].mean().unstack()
grouped_df.plot.line(title = 'Avg. 3P% Over Years(2004-2024) by Position', figsize=(20,8), legend = True)
plt.xticks(np.arange(2004, 2025, 1.0))

#%% load measurement data

measurement_df = pd.read_csv('C:/Users/Zachary Chan/Downloads/Basketball Project/measurements.csv')


#%% view data

measurement_df.columns
measurement_df.head()
measurement_df.describe()

#%% clean 'draft_year' column

measurement_df = measurement_df.drop(measurement_df[measurement_df.draft_year == 'Undrafted'].index)


#%%
measurement_df.draft_year = pd.to_numeric(measurement_df.draft_year, errors='coerce')

type(measurement_df['draft_year'][1])
#%% plot avg height over years
grouped_df = measurement_df.groupby('draft_year').mean('player_height')
grouped_df['player_height']

new_df = grouped_df.iloc[26:]
new_df.plot.line(y = 'player_height', title = 'Avg. Height Over Years', figsize = (20, 8))
plt.xticks(np.arange(2002, 2023, 1.0))

#%% plot avg weight over years
grouped_df = measurement_df.groupby('draft_year').mean('player_weight')
grouped_df['player_weight']

new_df = grouped_df.iloc[26:]
new_df.plot.line(y = 'player_weight', title = 'Avg. Weight Over Years', figsize = (20, 8))
plt.xticks(np.arange(2002, 2023, 1.0))

#%% histogram of 2002 height
filtered_df = measurement_df[measurement_df['draft_year'] == 2002]
filtered_df['draft_year']

height_df_2002 = filtered_df['player_height']
height_df_2002
plt.hist(height_df_2002, bins = 20)
plt.title('Histogram of Player Heights (2002)')
plt.xticks(np.arange(180, 235, 5))
#%% histogram of 2022 height
filtered_df = measurement_df[measurement_df['draft_year'] > 2018]
filtered_df['draft_year']

height_df_2022 = filtered_df['player_height']
height_df_2022
plt.hist(height_df_2022, bins = 20)
plt.title('Histogram of Player Heights (After 2019)')
plt.xticks(np.arange(180, 235, 5))

#%% histogram of 2002 weight
filtered_df = measurement_df[measurement_df['draft_year'] == 2002]
filtered_df['draft_year']

weight_df_2002 = filtered_df['player_weight']
weight_df_2002
plt.hist(weight_df_2002, bins = 20)
plt.title('Histogram of Player Weights (2002)')
plt.xticks(np.arange(70, 145, 5))

#%% histogram of 2022 weight
filtered_df = measurement_df[measurement_df['draft_year'] > 2018]
filtered_df['draft_year']

weight_df_2022 = filtered_df['player_weight']
weight_df_2022
plt.hist(weight_df_2022, bins = 20)
plt.title('Histogram of Player Weights (After 2019)')
plt.xticks(np.arange(70, 145, 5))