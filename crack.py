import zipfile
from threading import Thread
import argparse
import os

if not os.path.exists(os.path.join('passwords.txt')):
    with open("passwords.txt", 'w') as f:
        pass


def extract_zip(orignal_file_path, extract_file_path, zfile, password):
    extract_file_name = os.path.splitext(extract_file_path)[0]
    try:
        zfile.extractall(extract_file_name, pwd=bytes(password.encode()))
        print("[+] Password Found: "+password+'\n')

        with open("passwords.txt", 'a') as p:
            line = f"File Name :{orignal_file_path} Password :{password}\n"
            p.write(line)
    except Exception as e:
        pass


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, metavar='',
                    required=True, help="Zip File path")
parser.add_argument('-w', '--word_list', type=str, metavar='',
                    required=True, help="Word list path")
parser.add_argument('-e', "--extract_name", metavar='',
                    help='Folder name for extracted files (Default: with zip name)')
args = parser.parse_args()
orignal_file_path = args.file
wordlist = args.word_list
zfile = zipfile.ZipFile(orignal_file_path)
extract_file_path = orignal_file_path
if args.extract_name:
    folder_path = os.path.dirname(orignal_file_path)
    extract_file_path = os.path.join(folder_path, args.extract_name)

passfile = open(wordlist)
for line in passfile.readlines():
    password = line.strip('\n')
    t = Thread(target=extract_zip, args=(
        orignal_file_path, extract_file_path, zfile, password))
    t.start()
