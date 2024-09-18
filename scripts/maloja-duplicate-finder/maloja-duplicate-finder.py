import sqlite3
import pandas as pd
from tqdm import tqdm

def find_repetitions(df, tracks_df, min_repetitions=10):
    """Finds instances where a track is played more than a certain number of times consecutively.

    Args:
        df: A Pandas DataFrame containing the scrobbles data.
        tracks_df: A Pandas DataFrame containing the track metadata.
        min_repetitions: The minimum number of consecutive plays for a repetition to be counted.

    Returns:
        A list of dictionaries, where each dictionary represents a repetition and contains:
            - start_timestamp: The start timestamp of the repetition as a datetime object.
            - end_timestamp: The end timestamp of the repetition as a datetime object.
            - track_id: The ID of the repeated track.
            - count: The number of times the track was repeated.
            - start_unix: The start timestamp of the repetition as a Unix timestamp.
            - end_unix: The end timestamp of the repetition as a Unix timestamp.
            - track_title: The title of the repeated track.
    """

    repetitions = []
    current_track = None
    count = 0
    start_time = None

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing data"):
        if row['track_id'] == current_track:
            count += 1
        else:
            if count >= min_repetitions:
                repetitions.append({'start_timestamp': start_time, 'end_timestamp': row['timestamp'], 'track_id': current_track, 'count': count, 'start_unix': start_time.timestamp(), 'end_unix': row['timestamp'].timestamp()})
            current_track = row['track_id']
            count = 1
            start_time = row['timestamp']

    # Join with track titles
    df_result = pd.DataFrame(repetitions)
    df_result = df_result.merge(tracks_df, left_on='track_id', right_on='id', how='left')

    return df_result

# Connect to the SQLite database
conn = sqlite3.connect('malojadb.sqlite')

# Load data into Pandas DataFrames
df_scrobbles = pd.read_sql_query("SELECT timestamp, track_id FROM scrobbles", conn)
df_tracks = pd.read_sql_query("SELECT id, title FROM tracks", conn)

# Convert timestamp to datetime and sort
df_scrobbles['timestamp'] = pd.to_datetime(df_scrobbles['timestamp'], unit='s')
df_scrobbles = df_scrobbles.sort_values('timestamp')

# Find repetitions
repetitions = find_repetitions(df_scrobbles, df_tracks)

# Save results to a CSV file
repetitions.to_csv('repetitions_with_timestamps.csv', index=False)

print("Results saved to 'repetitions_with_timestamps.csv'")