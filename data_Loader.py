import pandas as pd

df = pd.read_csv('data/raw/dataset.csv')

columns_to_keep = [
    'track_id', 'artists', 'album_name', 'track_name',
    'popularity',
    'duration_ms',                                          # you like long songs
    'danceability', 'energy', 'key', 'loudness', 'mode',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo', 'time_signature',
    'track_genre'
]
df = df[columns_to_keep].dropna()  # drop rows with missing values
print(df.shape)  # check new shape after dropping missing values
print(df.head())

# Save cleaned version
df.to_csv('data/processed/dataset_clean.csv', index=False)