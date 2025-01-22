import csv, os, webbrowser, winsound

class utils():
    def __init__(self): # constructor
        pass

    def open_csv_file(csv_file_name):
        full_path = os.path.abspath(csv_file_name)
        csv_link = f'file://{full_path}'
        print(f'\noutput_scraping_csv_file: {csv_link}')
        assert os.path.getsize(csv_file_name) > 0, f"File '{csv_file_name}' is empty."
        user_input = input("\nWould you like to open the CSV file? (type 'y' for yes): ")
        if user_input == 'y':
            webbrowser.open(csv_link)  # open the csv file on screen

    def play_sound(rington):
        winsound.PlaySound(rington, winsound.SND_FILENAME)

    def csv_write_row(csv_file, field_values):
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(field_values)  # add the scraped data to csv
        # csv_file.flush() #Remark in real time
