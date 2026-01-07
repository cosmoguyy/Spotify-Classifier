panda is imported as pd kiddo
1) List vs Series

#list
energy_list = [0.8, 0.4, 0.9]

# pandas
energy_series = pd.Series([0.8, 0.4, 0.9])
print(energy_series.mean()) 

2) Dictionary to Dataframe transition

song_data = {
    'title': ['Song A', 'Song B'],
    'valence': [0.9, 0.2]
}
df = pd.DataFrame(song_data) # turns dictionary into a spreadsheet

3) Instead of If #else we use this 
# Shows only the 'Happy' songs (valence > 0.5)
happy_songs = df[df['valence'] > 0.5]
print(happy_songs)

4)#checking for missing value
print(df.isna().sum())

5)Data Handling

import pandas as pd

data = {
    'song': ['Blinding Lights', 'Stay', 'Levitating'],
    'energy': [0.8, 0.76, 0.82],
    'valence': [0.33, 0.59, 0.91]
}

df = pd.DataFrame(data)
print("My First DataFrame:")
print(df)

6) peeking at the Data

print("Top 5 Songs:")
print(df.head(5))

print("\nBottom 5 Songs:")
print(df.tail(5))

7) syntax for counting number of missing values

# This counts how many empty spots are in each column
missing_counts = df.isnull().sum()
print("Missing values per column:")
print(missing_counts)

8)# Filling missing values with the average value

avg_energy = df['energy'].mean()
df['energy'] = df['energy'].fillna(avg_energy)
print("Missing values filled!")
