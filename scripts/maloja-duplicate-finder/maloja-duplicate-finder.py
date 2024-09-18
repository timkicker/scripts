import sqlite3
import pandas as pd
from tqdm import tqdm

# Connect to the SQLite database
conn = sqlite3.connect('malojadb.sqlite')

# Load data into a Pandas DataFrame
df = pd.read_sql_query("SELECT timestamp, track_id FROM scrobbles", conn)

# Convert timestamp to datetime and sort
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df = df.sort_values('timestamp')

def find_repetitions(df, min_repetitions=10):
    """Finds instances where a track is played more than a certain number of times consecutively.

    Args:
        df: A Pandas DataFrame containing the scrobbles data.
        min_repetitions: The minimum number of consecutive plays for a repetition to be counted.

    Returns:
        A list of dictionaries, where each dictionary represents a repetition and contains:
            - start_timestamp: The start timestamp of the repetition as a datetime object.
            - end_timestamp: The end timestamp of the repetition as a datetime object.
            - track_id: The ID of the repeated track.
            - count: The number of times the track was repeated.
            - start_unix: The start timestamp of the repetition as a Unix timestamp.
            - end_unix: The end timestamp of the repetition as a Unix timestamp.
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

    return repetitions

# Find repetitions
result = find_repetitions(df)

# Save results to a CSV file
df_result = pd.DataFrame(result)
df_result.to_csv('repetitions_with_timestamps.csv', index=False)

print("Results saved to 'repetitions_with_timestamps.csv'")