import csv
import os
import webbrowser
import winsound


class utils():
    def __init__(self): # constructor
        pass

    def open_csv_file(csv_file_name):
        full_path = os.path.abspath(csv_file_name)
        csv_link = f'file://{full_path}'
        print(f'\noutput_scraping_csv_file: {csv_link}')
        user_input = input("\nWould you like to open the CSV file? (type 'y' for yes): ")
        if user_input == 'y':
            webbrowser.open(csv_link)  # open the csv file on screen

    def play_sound(rington):
        winsound.PlaySound(rington, winsound.SND_FILENAME)
