# BrutCracker
A normal password cracking tool which uses dictionary attack to crack weak passwords for any sha256(utf-8) hash.



______            _   _____                _             
| ___ \          | | /  __ \              | |            
| |_/ /_ __ _   _| |_| /  \/_ __ __ _  ___| | _____ _ __ 
| ___ \ '__| | | | __| |   | '__/ _` |/ __| |/ / _ \ '__|
| |_/ / |  | |_| | |_| \__/\ | | (_| | (__|   <  __/ |   
\____/|_|   \__,_|\__|\____/_|  \__,_|\___|_|\_\___|_|   
                                                         
 
================================================================================================================
BEFORE USING
================================================================================================================

EXECUTE THE BrutCracker.py file

1) This is a normal password cracking tool which uses SHA256(utf-8) encoding to decode the hashes to reveal the password.
2) The 'common_passwords.txt' file contains over 10 million frequently used passwords. The script uses these passwords to 
cross check with the provided hash to find the real password.
3) An additional tool (Hash_creator) is also provided to create SHA256 hashes for your desired password string.
4) Both of the tools are python based and you will need to have python installed. For Linux users, this is not a problem. 
   But for Windows users, this might be a hassle.
5) You need to enter you "username" and "hash" into the "username_hashes_combi.txt" file to crack the password.
6) The combination should be entered in the syntax:
                                username:hash

================================================================================================================
DISCLAIMER
================================================================================================================
The developer of this tool is not responsible for any malicious intent that the users may posses.
