import zipfile
from threading import Thread
import argparse
import os


def extract_zip(file_path, zfile, password):
    extract_file_name = os.path.splitext(file_path)[0]
    try:
        zfile.extractall(extract_file_name, pwd=bytes(password.encode()))
        print("[+] Password Found: "+password+'\n')
    except Exception as e:
        print(e)


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, metavar='',
                    required=True, help="Zip File path")
parser.add_argument('-w', '--word_list', type=str, metavar='',
                    required=True, help="Word list path")
parser.add_argument('-e', "--extract_name", metavar='',
                    help='Folder name for extracted files (Default: with zip name)')
args = parser.parse_args()
file_path = args.file
wordlist = args.word_list
print(file_path, wordlist)
zfile = zipfile.ZipFile(file_path)
if args.extract_name:
    file_path = os.path.join(args.extract_name)

passfile = open(wordlist)
for line in passfile.readlines():
    password = line.strip('\n')
    t = Thread(target=extract_zip, args=(file_path, zfile, password))
    t.start()
