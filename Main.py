import cryptography
import base64
import os
from cryptography.fernet import Fernet
import ast


# !!!!! PUT THIS IN THE FILE YOU WANT TO SECRIFY, MAKES LIFE EASIER !!!!!

def process_file(raw_text):
    return
   

def gen_key():
    key = Fernet.generate_key()
    name_file = input("Give your key a name")
    with open("%s" % name_file ,'wb') as keyfile:
        keyfile.write(key)
        keyfile.close()
   
    return key

def read_key():
    key_name = input("whats the keyname")
    with open(key_name, 'rb') as key_file:
        key = key_file.read()
    return key

def lock_file(item, Fernet_object): #concatenate lines into one first
    results = []
    submit = []
    final_line = ''

    with open(item, 'r+') as lock_file:
        raw_text = lock_file.readlines()
        lock_file.seek(0)
        lock_file.truncate(0)
        for line in raw_text:
            if len(line) > 2:
                lock_file.write(str(Fernet_object.encrypt(line.encode())))
                lock_file.write('\n')
                #lock_file.close()
            
            #final_line+=str(line)
            #lock_file.close()
        
        
       
    return "Done"

def unlock_file(item, Fernet_object):
    array_prs = [[], []]
    submit = []
    results = []
    final_line = ''
    with open(item,'r+') as lock_file:
        enc_text = lock_file.readlines()
        print(len(enc_text))
        lock_file.seek(0)
        lock_file.truncate(0)
        for line in enc_text:
            if len(line) > 2:
                raw_decr = Fernet_object.decrypt(ast.literal_eval(line))
                final_line+=raw_decr.decode()
                #final_line+=str(ast.literal_eval(Fernet_object.decrypt(line.encode())))

              

        lock_file.write(final_line)
        
    return "Done - Decrypt"
       
   
new_key = input("Do you need a new key Y/N ")

# while new_key != Y || N, input("question")

key = gen_key() if new_key=="Y" else read_key()

# makes an object that apparently is what does the actual encryption
# has method to encrypt and decrypt (based on the key - one key to an object?)

action = input ("lock or unlock files - 1. lock 2. unlock")


 # next step - need to save all text, clear the file, encrypt/decrypt, then put
 # it back


if int(action)==1:
    print(key)
    Fernet_object = Fernet(key)
    for file in os.listdir():
        if file.endswith(".txt"):
            print(file)
            results=lock_file(file,Fernet_object)

else:
    print(key)
    Fernet_object = Fernet(key)
    for file in os.listdir():
        if file.endswith(".txt"):
            results=unlock_file(file,Fernet_object)
            print(results)
   

# ok, think I can get around this by reading and encrypting each line separately
# saving it as a normal text file w spaces. then read/decrypt the line as long
# as it's less than 0 (and only encrypt the line past a certain point
