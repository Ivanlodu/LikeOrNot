from data_Loader import df
df_grouped = df.groupby('track_id').agg({
    'artists': 'first',
    'album_name': 'first',
    'track_name': 'first',
    'popularity': 'first',
    'duration_ms': 'first',
    'danceability': 'mean',
    'energy': 'mean',
    'key': 'first',
    'loudness': 'mean',
    'mode': 'first',
    'speechiness': 'mean',
    'acousticness': 'mean',
    'instrumentalness': 'mean',
    'liveness': 'mean',
    'valence': 'mean',
    'tempo': 'mean',
    'time_signature': 'first',
    'track_genre': lambda x: list(x.unique())
}).reset_index()

print(df_grouped['track_genre'].head(10))
print(type(df_grouped['track_genre'].iloc[0]))
print(df['track_id'].duplicated().sum())
print(df_grouped.shape)