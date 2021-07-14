import cryptography
import base64
import os
from cryptography.fernet import Fernet


#Geohot vectors and tiny grad cherry comptuer

# !!!!! do all this with the click of a button !!!!!!!!!

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

    with open(item, 'r+b') as lock_file:
        raw_text = lock_file.readlines()
        lock_file.seek(0)
        lock_file.truncate(0)
        for line in raw_text:
            final_line+=str(line)  
        lock_file.write(Fernet_object.encrypt(final_line.encode()))
        lock_file.close()
       
    return results

def prep_text_file(block):
    wildcard = '\\'
    array_pairs = [[], []]
    start_ind = 0
    array_ind = 0
    #need to get indices of all escapes, then add escapes
    while block.find(wildcard, start_ind) != -1:
        array_pairs[0].append(block.find(wildcard, start_ind))
        start_ind = array_pairs[0][array_ind] + 1
        array_pairs[1].append(block.find(wildcard[::-1], start_ind))
        start_ind = array_pairs[1][array_ind] + 1
        array_ind += 1
    return array_pairs
   


# so, how do I wrie the unencrypted text back WITH the formatting? I think I need to
# spell it out via text then put it back? idk
def unlock_file(item, Fernet_object):
    array_prs = [[], []]
    submit = []
    results = []
    with open(item,'r+b') as lock_file:
        enc_text = lock_file.read()
        print(len(enc_text))
        #lock_file.seek(0)
        #lock_file.truncate(0)
        decrypt_text = Fernet_object.decrypt(enc_text)
        #print(len(decrypt_text))
        print(decrypt_text)
        print(array_prs)
        #lock_file.writelines(str(decrypt_text))
       
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
