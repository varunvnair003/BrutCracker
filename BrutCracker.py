import hashlib

user_hash_dict = {}

with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()    #gets the passwords_list from the "common_passwords.txt" file

with open('username_hashes_combi.txt','r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]  #seperates the username:hash combo and stores them in "username" and "hash" variables for easy computing
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash

for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashed_password == hash:
            print(f'HASH FOUND\n{username}:{password}')
