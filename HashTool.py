# Version 1.0.0 Hashing tool to hash text, 16/01/2024

import hashlib
import os
import time


def encryption_types(menu_of_items):
    def sha256_encryption():
        os.system('cls')
        SHA256 = hashlib.sha256(input('SHA256> ').encode(), usedforsecurity=True).hexdigest()
        print('Your SHA256 hash is:', SHA256)
        time.sleep(5)
        return menu()

    def sha1_encryption():
        os.system('cls')
        SHA1 = hashlib.sha1(input('SHA1> ').encode(), usedforsecurity=True).hexdigest()
        print('Your SHA1 hash is:', SHA1)
        time.sleep(5)
        return menu()

    def md5_encryption():
        os.system('cls')
        MD5 = hashlib.md5(input('MD5> ').encode(), usedforsecurity=True).hexdigest()
        print('Your MD5 hash is:', MD5)
        time.sleep(5)
        return menu()

    def sha512_encryption():
        os.system('cls')
        SHA512 = hashlib.sha512(input('SHA512> ').encode(), usedforsecurity=True).hexdigest()
        print('Your SHA512 hash is:', SHA512)
        time.sleep(5)
        return menu()

    if menu_of_items == '1':
        sha256_encryption()
    elif menu_of_items == '2':
        md5_encryption()
    elif menu_of_items == '3':
        sha1_encryption()
    elif menu_of_items == '4':
        sha512_encryption()


def menu():
    try:
        os.system('cls')
        menu_of_items = input('''                    
                                                   
    |   ## [HASH TOOL] ## - coolpancakes      
    |                                            
    |                                                   
    |   1) SHA256   
    |   2) MD5     
    |   3) SHA1                               
    |   4) SHA512                             
    |                                      
    |                                            
         /> ''')

        encryption_types(menu_of_items)
    except KeyboardInterrupt:
        print("\n\nExiting...")
    


menu()
