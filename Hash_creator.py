import hashlib
password = input("Enter the password/string for which you need the sha256(utf-8) hash : ")
hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(hash)