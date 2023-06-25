import sys
import os
import pyzipper
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',';',':','"',"'",'<','>','?',',','.','/','`','~']
all = small + capital + numbers + special
known_password = ['n', '_', '^', '`', 'W', '5']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6, '5':8}
file_path = "The_secret.zip"
def unlock_zip_file(file_path, password):
    print(password)
    try:
        with pyzipper.AESZipFile(file_path) as zip_file:
            zip_file.extractall(pwd=password.encode())
        print("File unlocked successfully!")
        sys.exit()
    except RuntimeError as e:
        if 'Bad password' in str(e):
            print("Invalid password. Failed to unlock the file.")
for i in all:
    known_password.insert(3,i)
    known_password.insert(6,i)
    break
print(known_password)
for i in all:
    for j in all:
        known_password[3] = i
        known_password[6] = j
        known_password_str = ''.join(known_password)
        unlock_zip_file(file_path, known_password_str)