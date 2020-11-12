import secrets
import string
import pyperclip
import os

os.system("cls")
os.system("title Just A Secure Pass Gen")
password_Length = int(input("\n\033[31m How Long Shall I Make Your Password?: ", )) 
print()


characters = string.ascii_letters + string.digits + "#$%&@"


finished_password = ''.join(secrets.choice(characters) for i in range(password_Length))

os.system("cls")
print(f"\n\033[31m Generated Password: {finished_password}") 
print("\n\033[31m I Have Decided To Do The Nice Thing And Save You Like 3 Seconds As I Have Already Copied The Password To Your Clipboard!")
os.system("pause >NUL")

pyperclip.copy(finished_password)
spam = pyperclip.paste() # because we're nice ;)
