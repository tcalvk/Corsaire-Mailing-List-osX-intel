import itertools
import csv
import os
import getpass
import pandas as pd
import requests
import io


def check_for_updates(current_version):
    url = "https://raw.githubusercontent.com/tcalvk/Corsaire-Mailing-List-osX-intel/master/version.csv" # Make sure the url is the raw version of the file on GitHub
    download = requests.get(url).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    new_version_raw = df.to_csv()
    new_version_str = new_version_raw[1:]
    new_version_num = float(new_version_str)
    if new_version_num > current_version:
        return 'yes'
    else: 
        return None


def create_list():
    user = getpass.getuser()
    directory = f'/Users/{user}/downloads/Mailing_Lists'
    filename = f'/Users/{user}/downloads/Mailing_Lists/create_list.csv'
    if not os.path.exists(directory):
        os.mkdir(directory)
        with open(f'/Users/{user}/downloads/Mailing_Lists/create_list.csv', "w") as filename:
            print()
    else:    
        if not os.path.exists(filename):
            with open(f'/Users/{user}/downloads/Mailing_Lists/create_list.csv', "w") as filename:
                print()
        else: 
            print()
    
    try: 
        directory_out = f'/Users/{user}/downloads/Mailing_Lists'
        filename_out = 'list.csv'
        file_in = os.path.join(directory, filename)
        file_out = os.path.join(directory_out, filename_out)
        file_temp = f'/Users/{user}/downloads/Mailing_Lists/_temp.csv'

        with open(file_in, "r", newline='') as f_input, \
                open(file_out, "a", newline='') as f_output, \
                open(file_temp, "w", newline='') as f_temp:
            
            csv_input = csv.reader(f_input)

            # Append first 50 rows to file_out
            csv.writer(f_output).writerows(itertools.islice(csv_input, 0, 500))

            # Write the remaining rows from file_in to file_temp
            csv.writer(f_temp).writerows(csv_input)

        # Rename f_temp to file_in, first remove existing file_in then rename temp file
        os.remove(file_in)
        os.rename(file_temp, file_in)
        return 'yes'
    except Exception:
        return 'no'
