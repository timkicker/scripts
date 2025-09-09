import csv
import argparse
import datetime
import os

def convert_row(row):
    """Converts a row of data from the input CSV file.

    Args:
        row: A list representing a row of data from the input CSV file.

    Returns:
        A string representing the converted row of data.
    """

    uts, utc_time, artist, artist_mbid, album, album_mbid, track, track_mbid = row

    # Convert the utc_time to a datetime object
    utc_time_obj = datetime.datetime.strptime(utc_time, "%d %b %Y, %H:%M")

    # Format the datetime object in the desired format
    formatted_time = utc_time_obj.strftime("%d %b %Y %H:%M%z")

    converted_row = f"{artist},{album},{track},{formatted_time}"
    return converted_row

def main():
    # Assuming the input file is in the same directory as the script
    input_file = "import.csv"
    # Get the full path of the input file
    input_file = os.path.abspath(input_file)
    # Check if the input file exists and is a file
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found or is not a file.")
        return

    output_file = "output.csv"

    with open(input_file, 'r') as input_file, open(output_file, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        next(reader)  # Skip the first row
        for row in reader:
            converted_row = convert_row(row)
            output_file.write(converted_row + '\n')


    print(f"Conversion completed. The output is saved in {output_file}.")

if __name__ == "__main__":
    main()