import zipfile
from threading import Thread

def extract_zip(zfile, password):
    try:
        zfile.extractall("Password Protected123", pwd=bytes(password.encode()))
        print("[+] Password Found: "+password+'\n')
    except Exception as e:
        pass


zfile = zipfile.ZipFile("test.zip")
passfile = open('word_list.txt')
for line in passfile.readlines():
    password = line.strip('\n')
    t = Thread(target=extract_zip, args=(zfile, password))
    t.start()
