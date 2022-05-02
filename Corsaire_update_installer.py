#!/usr/bin/env python3
from concurrent.futures import process
from ftplib import FTP
import os
import sys
import time
import subprocess
import getpass

HOSTNAME = 'ftpupload.net'
USERNAME = 'epiz_31551663'
PASSWORD = 'LiqKBZjOFWC8zN'
USER = getpass.getuser()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def processDownload():
    print_slow("Download will begin shortly...")
    print()
    time.sleep(3)
    ftp_server = FTP()
    print_slow("Connecting to remote server...")
    print()
    time.sleep(3)
    ftp_server.connect(host = HOSTNAME)
    ftp_server.encoding = "utf-8"
    ftp_server.login(user = USERNAME, passwd = PASSWORD)
    downloadFilesList = ftp_server.nlst('htdocs/Corsaire Mailing List_osX intel')
    downloadFiles = downloadFilesList[2:]
    print_slow("Download may take 2-3 minutes. Don't exit the installer until complete...")
    print()
    time.sleep(2)
    print_slow("Downloading Updates...")
    print()

    if not os.path.exists(f'/Users/{USER}/Downloads/temp'):
        os.mkdir(f'/Users/{USER}/Downloads/temp')
    for downloadFile in downloadFiles:
        pathname = os.path.join(f'/Users/{USER}/Downloads/temp', downloadFile)
        with open(pathname, 'wb') as file :
            ftp_server.retrbinary('RETR %s' % f'htdocs/Email List App/{downloadFile}', file.write)
    print_slow("Almost done. Thank you for your patience...")
    print()
    time.sleep(5)
    ftp_server.close()
    print()
    print()
    print("Download complete. Installation will begin shortly. Do not shut down or restart your machine.")


def install_updates():
    subprocess.Popen(["open", "-a", '/Applications/DO NOT DELETE/Keka.app', f"/Users/{USER}/Downloads/temp/build.dmg.zip.001"])
    print("Finish installation by extracting the dmg file and installing the package.")
    #os.system('close Finder')


def main():
    processDownload()
    install_updates()




if __name__ == "__main__":
    main()